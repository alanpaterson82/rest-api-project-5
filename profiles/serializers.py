from rest_framework import serializers
from .models import Profile
from friends.models import Friend


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    friended_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    friends_count = serializers.ReadOnlyField()
    friended_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_friended_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            friended = Friend.objects.filter(
                owner=user, friended=obj.owner
            ).first()
            # print(friended)
            return friended.id if friended else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'friended_id',
            'posts_count', 'friends_count', 'friended_count',
        ]