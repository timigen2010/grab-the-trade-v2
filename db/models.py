from django.db import models


class Key(models.Model):
    key = models.CharField(max_length=255, unique=True)
    date_used = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class Resource(models.Model):
    url = models.URLField(max_length=255)


class Page(models.Model):
    url = models.URLField(max_length=255)
    date_used = models.DateTimeField(auto_now_add=True)

    resource = models.ForeignKey(Resource, null=True, on_delete=models.SET_NULL)


class ArticleCategory(models.Model):
    key = models.ForeignKey(Key, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    page = models.ForeignKey(Page, null=True, on_delete=models.SET_NULL)

