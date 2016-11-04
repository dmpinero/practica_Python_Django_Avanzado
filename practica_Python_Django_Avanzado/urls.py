from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from blogs import urls as blogs_urls, api_urls as blogs_api_urls
from django.conf.urls.static import static
from users import urls as users_urls, api_urls as users_api_urls
from fotos import api_urls as fotos_api_urls
from files import api_urls as files_api_urls

urlpatterns = [
    # Django admin URLs
    url(r'^admin/', include(admin.site.urls)),

    # Blogs URLs
    url(r'^', include(blogs_urls)),

    # Users URLs
    url(r'^', include(users_urls)),

    # API URLs
    url(r'^api/', include(blogs_api_urls)),
    url(r'^api/', include(users_api_urls)),
    url(r'^api/', include(files_api_urls)),
    url(r'^api/', include(fotos_api_urls)),

    # Autenticación con JWT
    url(r'^api/token-auth/', obtain_jwt_token),     # Obtener token
    url(r'^api/token-refresh/', refresh_jwt_token), # Refrescar token
    url(r'^api/token-verify/', verify_jwt_token),   # Verificar token

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # support for media files
