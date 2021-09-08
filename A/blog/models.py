from django.db import models
# import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    body = models.TextField(default=None)
    # default = datetime.datetime.now
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')

