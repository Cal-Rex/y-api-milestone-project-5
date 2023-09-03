from django.shortcuts import render
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from y_api.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate(
        votes_count=Count('parent_comment', distinct=True)
    )
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = ['votes_count', 'post']
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
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate(
        votes_count=Count('parent_comment', distinct=True)
    )
