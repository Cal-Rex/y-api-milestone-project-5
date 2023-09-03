from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from django.db import IntegrityError
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_image = serializers.ReadOnlyField(source='owner.image.url')
    followed_username = serializers.ReadOnlyField(source='followed.username')
    followed_user_image = serializers.ReadOnlyField(source='followed.image.url')
    is_owner = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_date_created(self, obj):
        return naturaltime(obj.date_created)
    
    def create(self, new_follow):
        try:
            return super().create(new_follow)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "IT'S POSSIBLE THIS FOLLOW PAIRING ALREADY EXISTS"
            })

    class Meta:
        model = Follow
        fields = [
            'id',
            'date_created',
            'owner',
            'owner_id',
            'owner_image',
            'followed',
            'followed_username',
            'followed_user_image',
            'is_owner',
        ]