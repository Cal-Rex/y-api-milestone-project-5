"""
serializer to create custom /
fields not natively stored in db models
serializes data into JSON compatible format
"""
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from likes.models import Like
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    serializes Post model data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    liked_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_date_created(self, obj):
        """
        amends date_created
        into more readable format
        """
        return naturaltime(obj.date_created)

    def get_date_updated(self, obj):
        """
        amends date_updated
        into more readable format
        """
        return naturaltime(obj.date_updated)

    def get_liked_id(self, obj):
        """
        gets the id of the like owned by
        a requesting user if the user
        likes the viewed post
        """
        user = self.context['request'].user
        if user.is_authenticated:
            liked = Like.objects.filter(owner=user, post=obj).first()
            if liked:
                return liked.id
            return None

    def create(self, validate_post):
        try:
            return super().create(validate_post)
        except ValueError:
            raise serializers.ValidationError({
                'detail': "You need to be signed in to do that, buddy!"
            })

    class Meta:
        """
        orders data returned to view
        by serializer
        """
        model = Post
        fields = [
            'id',
            'date_created',
            'date_updated',
            'owner',
            'profile_id',
            'profile_image',
            'title',
            'content',
            'image',
            'is_owner',
            'liked_id',
            'likes_count',
            'comments_count'
        ]
