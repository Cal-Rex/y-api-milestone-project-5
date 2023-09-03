from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'owner',
        'comment',
        'comment__votes_count'
    ]
    filterset_fields = [
        # filter by
        # votes by user
        'owner__profile',
        # votes on post
        'comment__post',
        # votes on comment
        'comment',
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
