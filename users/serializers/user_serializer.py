from django.contrib.auth.hashers import make_password

from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    #is_staff = serializers.ReadOnlyField()
    remove_intrests = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def update(self, instance, validated_data):
        if validated_data.get('remove_intrests'):
            intrests = validated_data.get('remove_intrests')
            for intrest in intrests:
                instance.intrests.remove(intrest)
        return super().update(instance, validated_data)