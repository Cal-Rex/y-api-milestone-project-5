"""
serializer to create custom /
fields not natively stored in db models
serializes data into JSON compatible format
"""
from rest_framework import serializers
from follows.models import Follow
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    serializes Profile model data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        gets the id of the follow owned by
        a requesting user if the user
        follows the viewed profile
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follow.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            if following:
                return following.id
        return None

    class Meta:
        """
        orders data returned to view
        by serializer
        """
        model = Profile
        fields = [
            'id',
            'date_created',
            'date_updated',
            'owner',
            'is_owner',
            'display_name',
            'bio',
            'image',
            'posts_count',
            'comments_count',
            'followers_count',
            'following_id',
            'following_count',
        ]
