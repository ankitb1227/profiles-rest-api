from rest_framework import serializers
from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
                         }
        }

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data['password']
            instance.set_password(password)

        return super().update(instance, validated_data)