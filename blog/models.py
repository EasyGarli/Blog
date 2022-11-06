from email.policy import default
import hashlib
import time
from unicodedata import category

from django.db import models


def _create_hash():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode('utf-8'))
    return  hash.hexdigest()[:]


class CategoryModel(models.Model):
    """Модель категории поста"""
    name = models.CharField(max_length=128, unique=True)
    eng_name = models.CharField(max_length=128, unique=True, default='category_name')
    image = models.ImageField(upload_to = 'blog/category_images')
    description = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class PostModel(models.Model):
    """Модель поста"""
    title = models.CharField(max_length=256, unique=True)
    main_image = models.ImageField(upload_to='blog/post_images')
    second_text = models.CharField(max_length=512)
    pub_date = models.DateField(auto_now=True)
    hash_field = models.CharField(max_length=40, default=_create_hash, unique=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(CategoryModel, related_name='posts', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " " + str(self.pub_date)


class InfoBlockModel(models.Model):
    """Модель блоков которые входят в состав поста"""
    sub_title = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/post_images', blank=True)
    order_number = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(PostModel, related_name='blocks', on_delete=models.CASCADE)