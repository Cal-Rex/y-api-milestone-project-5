from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = [
            'id',
            'date_created',
            'date_updated',
            'owner',
            'display_name',
            'bio',
            'image',
            'posts_count',
            'comments_count',
            'followers_count',
            'following_count',
        ]