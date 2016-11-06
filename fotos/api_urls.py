from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from fotos.views import FotoViewSet

router = DefaultRouter()
router.register('fotos', FotoViewSet)

urlpatterns = (
    url(r'^1.0/', include(router.urls)),
)