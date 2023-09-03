from rest_framework import serializers
from .models import Profile
from follows.models import Follow


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follow.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            if following:
                return following.id
            else: None
        return None

    class Meta:
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