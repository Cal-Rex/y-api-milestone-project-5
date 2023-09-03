from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.views import APIView
from .models import Vote
from .serializers import VoteSerializer
from y_api.permissions import IsOwnerOrReadOnly


class VoteList(generics.ListCreateAPIView):
    """
    List all of the votes that have been
    made on comments.
    see who votes on what comment from what post
    """
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
