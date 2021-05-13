from rest_framework import serializers

from materials.models import Scope


class ScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        fields = '__all__'
