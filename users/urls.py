from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views.general import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    ]

urlpatterns += router.urls