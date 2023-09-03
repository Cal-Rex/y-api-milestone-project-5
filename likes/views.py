from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Like
from .serializers import LikeSerializer
from y_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    List all of the likes that have been
    made on posts.
    see what post was liked and who owns
    the likes
    """
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()