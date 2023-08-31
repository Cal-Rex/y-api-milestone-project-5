from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Like
from .serializers import LikeSerializer


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