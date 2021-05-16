from rest_framework import serializers

from materials.models import Theme
from materials.services.serializer_helpers import add_remove_m2m_functional
from tags.serializers import TagSerializer


class ThemeSerializer(serializers.ModelSerializer):
    remove_tags = serializers.ListField(write_only=True, required=False)
    add_tags = serializers.ListField(write_only=True, required=False)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Theme
        fields = '__all__'

    def update(self, instance, validated_data):
        add_remove_m2m_functional(validated_data, instance.tags, 'add_tags', 'remove_tags')
        return super().update(instance, validated_data)
