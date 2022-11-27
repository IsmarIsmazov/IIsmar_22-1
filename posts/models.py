from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    likes = models.IntegerField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}, {self.text}'
