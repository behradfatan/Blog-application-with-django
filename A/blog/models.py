from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
