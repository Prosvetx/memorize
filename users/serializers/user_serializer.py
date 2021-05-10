from django.contrib.auth.hashers import make_password

from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        return make_password(value)
