"""
views for profiles app
"""
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import generics, filters, permissions
from y_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    functionality to order, filter
    and search db model
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        comments_count=Count('owner__comment', distinct=True)
    ).order_by('-date_created')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'comments_count',
        'owner__followed__date_created',
        'owner__following__date_created'
        ]
    search_fields = ['owner__username']
    filterset_fields = [
        # filter by:
        # profiles a user has followed
        'owner__following__followed__profile',
        # profiles that are following the user
        'owner__followed__owner__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a specific profile
    or, update a profile if you're the owner
    """
    permission_classes = permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        comments_count=Count('owner__comment', distinct=True)
    ).order_by('-date_created')
