from rest_framework.routers import DefaultRouter

from materials.views import ScopeViewSet
from materials.views import SubdivisionViewSet
from materials.views import ThemeViewSet

router = DefaultRouter()
router.register('scopes', ScopeViewSet)
router.register('subdivisions', SubdivisionViewSet)
router.register('themes', ThemeViewSet)

urlpatterns = [
    ]

urlpatterns += router.urls