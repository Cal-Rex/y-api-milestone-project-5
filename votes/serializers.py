"""
serializer to create custom /
fields not natively stored in db models
serializes data into JSON compatible format
"""
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    serializes Vote model data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_image = serializers.ReadOnlyField(source='owner.image.url')
    post = serializers.ReadOnlyField(source='comment.post.id')
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
        takes the date_created value
        and returns it in a relative time
        more readable for the user
        """
        return naturaltime(obj.date_created)

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "USER POSSIBLY ALREADY VOTED ON THIS COMMENT"
            })

    class Meta:
        """
        orders data returned to view
        by serializer
        """
        model = Vote
        fields = [
            'id',
            'date_created',
            'owner',
            'owner_id',
            'owner_image',
            'post',
            'comment',
            'is_owner',
    ]
