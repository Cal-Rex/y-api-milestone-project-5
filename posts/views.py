from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListAPIView):
    """
    List all profiles.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()