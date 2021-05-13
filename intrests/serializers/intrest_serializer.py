from rest_framework import serializers

from users.models import Intrest


class IntrestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Intrest
        fields = '__all__'

