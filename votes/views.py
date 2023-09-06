"""
views for votes app
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from y_api.permissions import IsOwnerOrReadOnly
from .models import Vote
from .serializers import VoteSerializer


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
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'owner',
        'comment',
        'comment__votes_count'
    ]
    search_fields = [
        'owner__username', 'comment__content'
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
    """
    detail view of a vote that
    gives owner options delete
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
