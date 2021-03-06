from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views.general import UserViewSet

from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

router = DefaultRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),

    ]

urlpatterns += router.urls
