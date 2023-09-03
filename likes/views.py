from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.views import APIView
from .models import Like
from .serializers import LikeSerializer
from y_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class LikeList(generics.ListCreateAPIView):
    """
    List all of the likes that have been
    made on posts.
    see what post was liked and who owns
    the likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'owner',
        'post',
        'post__likes_count',
        'post__comments_count'
    ]
    filterset_fields = [
        # filter by:
        # likes by user
        'owner__profile',
        # likes by post
        'post'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()