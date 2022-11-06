from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import CategorySerializer, PostDetailSerializer, PostsBriefListSerializer, CategoryDetailSerializer
from .models import CategoryModel, PostModel


class PostDetailView(APIView):
    """
    Вью для детального поста: получение, обновление, создание
    """
    def get_object(self,  hash):
        try:
            return PostModel.objects.get(hash_field=hash)
        except PostModel.DoesNotExist:
            raise Http404

    def get(self, request, hash, format=None):
        post = self.get_object(hash)
        post.views = post.views + 1
        post.save()
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class CategoryListView(generics.ListCreateAPIView):
    """Список категорий"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class PostsListView(generics.ListCreateAPIView):
    """Список постов"""
    queryset = PostModel.objects.all()
    serializer_class = PostsBriefListSerializer


class CategoryDetailView(APIView):
    """Ендпоинт детального отображения категории"""
    def get(self, request, category_name, format=None):
        category = CategoryModel.objects.get(eng_name=category_name)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)
