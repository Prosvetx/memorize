from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from materials.models import Scope, Subdivision, Theme
from materials.serializers.scope_serializers import ScopeSerializer
from materials.serializers.subdivision_serializers import SubdivisionSerializer
from materials.serializers.theme_serializers import ThemeSerializer


class ScopeViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ScopeSerializer
    queryset = Scope.objects.all()


class SubdivisionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()


class ThemeViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
