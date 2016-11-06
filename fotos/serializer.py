from rest_framework.serializers import ModelSerializer

from fotos.models import Foto


class FotoSerializer(ModelSerializer):

    class Meta:
        model = Foto
        read_only_fields = ('owner', )