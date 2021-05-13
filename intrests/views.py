from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers.intrest_serializer import IntrestSerializer

from users.models import Intrest


class IntrestsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Intrest.objects.all()
    serializer_class = IntrestSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

