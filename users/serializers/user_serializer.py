from django.contrib.auth.hashers import make_password

from materials.services.serializer_helpers import add_remove_m2m_functional
from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    #is_staff = serializers.ReadOnlyField()
    remove_intrests = serializers.ListField(write_only=True, required=False)
    add_intrests = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def update(self, instance, validated_data):
        add_remove_m2m_functional(validated_data, instance.intrests, 'add_intrests', 'remove_intrests')
        return super().update(instance, validated_data)