#TODO. Versionar APIs
from rest_framework.routers import SimpleRouter

from fotos.views import FotoViewSet

router = SimpleRouter()
router.register(r'fotos', FotoViewSet)

urlpatterns = router.urls