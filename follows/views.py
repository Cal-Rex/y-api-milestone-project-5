"""
views for follows app
"""
from rest_framework import generics, permissions
from y_api.permissions import IsOwnerOrReadOnly
from .models import Follow
from .serializers import FollowSerializer


class FollowList(generics.ListCreateAPIView):
    """
    List all follow links between users.
    and, create a follow link between
    the authenticated user and other user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a specific follow instance
    Destroy follow option if owner of the follow 
    viewing
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
