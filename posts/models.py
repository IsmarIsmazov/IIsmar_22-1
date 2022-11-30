from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', null=True, blank=True)

    def str(self):
        return self.title

class Category(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
RATE =((i, '★' * i) for i in range(1, 6))

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    rate = models.IntegerField(choices=RATE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}, {self.text}'
