from django.core.management import BaseCommand

from fotos.models import Foto
from fotos.util import generate_responsive_images


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Fetching photos to resize its images")
        fotos = Foto.objects.filter(image_resized=False)
        self.stdout.write("{0} photos to resize its images".format(fotos.count()))
        for foto in fotos:
            self.stdout.write("Resizing photo {0} image".format(foto.pk))
            generate_responsive_images(foto)
            foto.image_resized = True  # Marcar imagen como ya procesada
            foto.save()                # Guardar foto
            self.stdout.write(self.style.SUCCESS("Photo {0}'s image resized successfully".format(foto.pk)))