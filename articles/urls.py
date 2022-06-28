from django.urls import path

from . import views

urlpatterns = [
    path('list', views.listArticle),
    path('find', views.findArticle),
    path('my', views.myArticle),
    path('create', views.createArticle),
    path('calculateSummary', views.calculateSummary),
    path('calculateTags', views.calculateTags),
    path('fileUpload', views.fileUpload),
    path('related', views.relatedArticle),
]
