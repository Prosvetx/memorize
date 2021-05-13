from django.conf.urls.static import static
from config import settings
from django.urls import path

from images.views import ImageListCreateView, ImageUDDView

urlpatterns = [
    path('<int:pk>/', ImageUDDView.as_view()),
    path('', ImageListCreateView.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
