from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import CategoryModel, PostModel, InfoBlockModel

class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели категории"""
    class Meta:
        model = CategoryModel
        fields = "__all__"


class InfoBlockSerializer(serializers.ModelSerializer):
    """Сериализатор модели блока для поста"""
    class Meta:
        model = InfoBlockModel
        fields = "__all__"


class PostDetailSerializer(serializers.ModelSerializer):
    """Сериализатор модели поста подробный"""

    blocks = InfoBlockSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = PostModel
        fields = ("title", "main_image", "second_text", "pub_date", "hash_field", "blocks", "views", "category")


class PostsBriefListSerializer(serializers.ModelSerializer):
    """Сериализатор для кратого отображения инф поста"""

    class Meta:
        model = PostModel
        fields = ("title", "main_image", "second_text", "hash_field")


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Сериализатор страницы категории"""

    posts = PostsBriefListSerializer(many=True)

    class Meta:
        model = CategoryModel
        fields = ("name", "image", "description", "posts")