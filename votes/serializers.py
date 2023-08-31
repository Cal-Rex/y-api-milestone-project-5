from rest_framework import serializers
from django.db import IntegrityError
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_image = serializers.ReadOnlyField(source='owner.image.url')
    post = serializers.ReadOnlyField(source='comment.post')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def create(self, new_vote):
        try:
            return super().create(new_vote)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "USER POSSIBLY ALREADY VOTED ON THIS COMMENT"
            })
    
    class Meta:
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