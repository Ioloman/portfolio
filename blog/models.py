from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    article = models.TextField()
