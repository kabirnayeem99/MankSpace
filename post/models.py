from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model


class Category(models.Model):
    # Category class which contains
    # name of the category 
    # and cover page of the category
    name = models.CharField(max_length=60)
    category_cover = models.CharField(max_length=60)

    # Constructor will only take the name of the category
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self): # This will show post title along with its author (kabir)
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)]) # Will return to new created post


class Comment(models.Model):
    article = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=439)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_list')
