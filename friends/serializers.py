from django.db import IntegrityError
from rest_framework import serializers
from .models import Friend


class FriendSerializer(serializers.ModelSerializer):
    """
    Serializer for the Friend model
    Create method handles the unique constraint on 'owner' and 'friended'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    friended_name = serializers.ReadOnlyField(source='friended.username')

    class Meta:
        model = Friend
        fields = [
            'id', 'owner', 'created_at', 'friended', 'friended_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})