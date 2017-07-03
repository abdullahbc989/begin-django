from django.db import models

# Create your models here.


class Author(models.Model):
    name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = None
    content = models.TextField()
    pub_date = models.DateTimeField()
