from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    post_title = serializers.ReadOnlyField(source='post.title')
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
            'votes_count',
            'is_owner',
        ]