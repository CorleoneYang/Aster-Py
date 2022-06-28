from django.db import models


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    thumbUrl = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    tags = models.JSONField()

    def __self__(self, title, summary, thumbUrl, author, time, content, tags):
        self.title = title
        self.summary = summary
        thumbUrl = thumbUrl
        author = author
        time = time
        content = content
        tags = tags



