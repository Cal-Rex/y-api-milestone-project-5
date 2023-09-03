from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    is_owner = serializers.SerializerMethodField()
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
    
    def create(self, validate_post):
        try:
            return super().create(validate_post)
        except ValueError:
            raise serializers.ValidationError({
                'detail': "You need to be signed in to do that, buddy!"
            })

    class Meta:
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
            'likes_count',
            'comments_count'
        ]