from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Follow
from .serializers import FollowSerializer
from y_api.permissions import IsOwnerOrReadOnly


class FollowList(generics.ListCreateAPIView):
    """
    List all follow links between users.
    and, create a follow link between
    the authenticated user and other user.
    """
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
