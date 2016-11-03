from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from fotos.serializer import FotoSerializer
from fotos.models import Foto
from fotos.util import generate_responsive_images


class FotoViewSet(ModelViewSet):

    serializer_class = FotoSerializer
    queryset = Foto.objects.all()
    permission_classes = (IsAuthenticated, )

    # Al crear o actualizar una foto el propietario será el usuario autenticado
    def perform_create(self, serializer):
        foto = serializer.save(owner=self.request.user)
        generate_responsive_images(foto)

    def perform_update(self, serializer):
        foto = serializer.save(owner=self.request.user)
        generate_responsive_images(foto)