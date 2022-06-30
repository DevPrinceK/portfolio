from django.db import models
from accounts.models import User


class Blog(models.Model):
    '''Model for creating blog posts'''
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# model for works - image, title, summary
class Work(models.Model):
    '''Model for storing my works'''
    image = models.ImageField(upload_to='works/')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)

    def __str__(self):
        return self.title


# model for caterogies - name, description
class Category(models.Model):
    '''Model for blog categories'''
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


# tags - name
class Tag(models.Model):
    '''Model for blog tags'''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# clients  - name, image
class Client(models.Model):
    '''Model for clients'''
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name
