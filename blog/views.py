from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# def tag_list(request):
#     tags = Tag.objects.all()
#     return render(request, "blog/tag_list.html", {"tags": tags})


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug=slug)
#     posts = Post.objects.filter(tags=tag)
#     return render(request, "blog/tag_detail.html", {"tag": tag, "posts": posts})
