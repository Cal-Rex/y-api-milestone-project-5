"""
serializer to create custom /
fields not natively stored in db models
serializes data into JSON compatible format
"""
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    """
    serializes Follow model data
    """
    owner = serializers.ReadOnlyField(
        source='owner.username'
    )
    owner_id = serializers.ReadOnlyField(
        source='owner.id'
    )
    owner_image = serializers.ReadOnlyField(
        source='owner.image.url'
    )
    followed_username = serializers.ReadOnlyField(
        source='followed.username'
    )
    followed_user_image = serializers.ReadOnlyField(
        source='followed.image.url'
    )
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
        """
        amends date_created
        into more readable format
        """
        return naturaltime(obj.date_created)

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "IT'S POSSIBLE THIS FOLLOW PAIRING ALREADY EXISTS"
            })

    class Meta:
        """
        orders data returned to view
        by serializer
        """
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
