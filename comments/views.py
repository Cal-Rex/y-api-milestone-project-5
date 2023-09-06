"""
views for comments app
"""
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from y_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer



class CommentList(generics.ListCreateAPIView):
    """
    List all of the comments 
    that have been made by users
    authenticated users can create new comments
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate(
        votes_count=Count('parent_comment', distinct=True)
    )
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = ['votes_count', 'post']
    search_fields = ['post__title', 'owner__username']
    filterset_fields = [
        # filter by:
        # comments by a user
        'owner__profile',
        # comments by post
        'post',
        # comments user has voted on
        'parent_comment__owner'
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a specific comment
    edit or Destroy comment if owner of the comment
    viewing
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate(
        votes_count=Count('parent_comment', distinct=True)
    )
