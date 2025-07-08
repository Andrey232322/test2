
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_avatar_url(self, obj):
        if obj.avatar:
            return obj.avatar.storage.url(obj.avatar.name)
        return None