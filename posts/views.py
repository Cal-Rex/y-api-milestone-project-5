"""
views for profiles app
"""
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import generics, filters, permissions
from y_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView):
    """
    List all posts
    filter posts
    and, create a post
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        likes_count = Count('liked_post', distinct=True),
        comments_count = Count('parent_post', distinct=True),
    ).order_by('-date_created')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = ['likes_count', 'comments_count']
    search_fields = ['owner__username', 'title']
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
        serializer.save(owner=self.request.user)


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