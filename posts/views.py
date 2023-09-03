from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from y_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List all posts.
    and, create a post
    """
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        likes_count = Count('liked_post', distinct=True),
        comments_count = Count('parent_post', distinct=True),
    ).order_by('-date_created')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = ['likes_count', 'comments_count']
    filterset_fields = [
        # filter by:
        # posts by a followed user
        'owner__followed__owner__profile',
        # posts by user
        'owner__profile',
        # posts user has liked
        'liked_post__owner__profile',
        # posts user has commented on
        'parent_post__owner__profile',
    ]
    

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except ValueError:
            return Response({
        "error": "You need to be signed in to do that buddy!"
    })
        


class PostDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a specific post
    or, update a post if you're the owner
    """
    permission_classes = permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        likes_count = Count('liked_post', distinct=True),
        comments_count = Count('parent_post', distinct=True),
    ).order_by('-date_created')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['likes_count', 'comments_count']