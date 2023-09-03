from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from django.db import IntegrityError
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_image = serializers.ReadOnlyField(source='owner.image.url')
    post_id = serializers.ReadOnlyField(source='post.id')
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
    
    def create(self, validate_like):
        try:
            return super().create(validate_like)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "IT'S POSSIBLE THIS USER ALREADY LIKES THIS POST"
            })

    class Meta:
        model = Like
        fields = [
            'id',
            'date_created',
            'post',
            'post_id',
            'owner',
            'owner_id',
            'owner_image',
            'is_owner',
        ]