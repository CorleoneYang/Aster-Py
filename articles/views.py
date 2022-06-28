import json
import random

from django import forms
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from articles.models import Article


def listArticle(request):
    data = json.loads(request.body.decode('utf-8'))
    tag = data.get('tag', None)
    keyword = data.get('keyword', None)
    articles = Article.objects.values()
    if tag is not None and tag != 'All':
        # 筛选 tags 中是否存在所筛选的 tag
        articles = filter(lambda item: (tag in item['tags']), articles)
    if keyword is not None:
        articles = articles.filter(title__contains=keyword)
    return JsonResponse(list(articles), safe=False)


def findArticle(request):
    data = json.loads(request.body.decode('utf-8'))
    search_id = data.get('id')
    article = Article.objects.filter(id__exact=search_id).values().first()
    return JsonResponse(article, safe=False)


def myArticle(request):
    data = json.loads(request.body.decode('utf-8'))
    keyword = data.get('keyword', None)
    articles = Article.objects.values()
    if keyword is not None:
        articles = articles.filter(title__contains=keyword)
    # 以后可以把用户 ID 作为参数传递，查询自己写的文章
    res = list(articles)
    return JsonResponse(res, safe=False)


def createArticle(request):
    data = json.loads(request.body.decode('utf-8'))
    title = data.get('title', '')
    content = data.get('content', '')
    summary = data.get('summary', '')
    thumbUrl = data.get('url', '')
    tags = data.get('tags', [])
    article = Article(title=title, content=content, summary=summary, tags=tags, thumbUrl=thumbUrl)
    article.save()
    return JsonResponse(Article.objects.filter(id=article.id).values().first(), safe=False)


def relatedArticle(request):
    data = json.loads(request.body.decode('utf-8'))
    searchId = data.get('title', None)
    # todo: 这里搜索推荐相关文章
    articles = Article.objects.values()

    return JsonResponse(list(articles), safe=False)


def calculateSummary(request):
    data = json.loads(request.body.decode('utf-8'))
    title = data.get('title', '')
    content = data.get('content', '')
    # todo: 这里根据模型生成摘要
    summary = "测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试"
    response = {
        'summary': summary
    }
    return HttpResponse(json.dumps(response), content_type="application/json")


def calculateTags(request):
    data = json.loads(request.body.decode('utf-8'))
    title = data.get('title', '')
    content = data.get('content', '')

    # todo: 这里根据模型生成标签
    tags = ['Android', 'Flutter', 'OpenCV', 'Pytorch', 'TensorFlow', 'Caffe']

    return HttpResponse(json.dumps(tags), content_type="application/json")


def fileUpload(request):
    file = request.FILES['file']
    path = f"static/{random.randint(0, 99999)}{file.name}"

    with open(path, 'wb+') as destination:
        for chunk in request.FILES['file'].chunks():
            destination.write(chunk)

    return HttpResponse(json.dumps({
        'url': "http://" + request.META['HTTP_HOST'] + '/' + path
    }), content_type="application/json")
