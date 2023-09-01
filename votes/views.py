from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Vote
from .serializers import VoteSerializer


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
