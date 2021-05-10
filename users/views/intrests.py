from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.serializers.intrest_serializer import IntrestSerializer

from users.models import Intrest


class IntrestsViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Intrest.objects.all()
    serializer_class = IntrestSerializer
    http_method_names = ['get', 'post', 'delete', 'put']

