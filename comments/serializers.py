from rest_framework import serializers
from .models import Comment
from votes.models import Vote

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    post_title = serializers.ReadOnlyField(source='post.title')
    voted_on_id = serializers.SerializerMethodField()
    votes_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

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