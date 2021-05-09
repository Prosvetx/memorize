from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
