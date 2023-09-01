from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        comments_count=Count('owner__comment', distinct=True)
    ).order_by('-date_created')
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'comments_count',
        'owner__followed__date_created',
        'owner__following__date_created'
        ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a specific profile 
    or, update a profile if you're the owner
    """
    # permission_classes = 
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
