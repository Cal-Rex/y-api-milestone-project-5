from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from y_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    List all profiles.
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
        # users following profile
        'owner__following__followed__profile',
        # profiles following user
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
