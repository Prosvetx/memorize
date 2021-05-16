from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tags.models import Tag
from tags.serializers import TagSerializer


class TagsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
