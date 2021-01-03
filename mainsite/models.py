from django.db import models

# Create your models here.
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class company(models.Model):
    time = models.CharField(max_length=1000, null=False)
    place = models.CharField(max_length=1000, default='M', null=False)
    people = models.CharField(max_length=1000, default='M', null=False)
    car = models.CharField(max_length=1000, blank=True, default='')
    longitude = models.CharField(max_length=1000, blank=True, default='')
    latitude = models.CharField(max_length=1000, blank=True, default='')
    def __str__(self):
        return self.time


