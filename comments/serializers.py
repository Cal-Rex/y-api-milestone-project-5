"""
serializer to create custom /
fields not natively stored in db models
serializes data into JSON compatible format
"""
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from votes.models import Vote
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    serializes Comment model data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    post_title = serializers.ReadOnlyField(source='post.title')
    voted_on_id = serializers.SerializerMethodField()
    votes_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_voted_on_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            voted = Vote.objects.filter(owner=user, comment=obj).first()
            if voted:
                return voted.id
            else: None

    def get_date_created(self, obj):
        return naturaltime(obj.date_created)
        
    def get_date_updated(self, obj):
        return naturaltime(obj.date_updated)
    
    def create(self, validate_comment):
        try:
            return super().create(validate_comment)
        except ValueError:
            raise serializers.ValidationError({
                'detail': "You need to be signed in to do that, buddy!"
            })
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'date_created',
            'date_updated',
            'owner',
            'profile_id',
            'profile_image',
            'post',
            'post_title',
            'content',
            'voted_on_id',
            'votes_count',
            'is_owner',
        ]