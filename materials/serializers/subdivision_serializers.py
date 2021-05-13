from rest_framework import serializers

from materials.models import Subdivision


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'
