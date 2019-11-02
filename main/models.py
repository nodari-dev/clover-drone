# Create your models here.
from django.db import models
from datetime import datetime

class News(models.Model):
    title_news = models.CharField(max_length=200)
    content_news = models.TextField()
    published_news = models.DateTimeField('Data pusblihed', default=datetime.now())

    def __str__(self):
        return self.title_news


class Updates(models.Model):
    title_updates = models.CharField(max_length=200)
    content_updates = models.TextField()
    published_updates = models.DateTimeField('Data pusblihed', default=datetime.now())

    def __str__(self):
        return self.title_updates