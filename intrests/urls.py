from rest_framework.routers import DefaultRouter

from intrests.views import IntrestsViewSet

router = DefaultRouter()
router.register('', IntrestsViewSet)

urlpatterns = [

    ]

urlpatterns += router.urls