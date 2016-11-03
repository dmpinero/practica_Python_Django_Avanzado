from celery import shared_task
from easy_thumbnails.files import generate_all_aliases


@shared_task
def generate_responsive_images(foto):
    generate_all_aliases(foto.image, True)
    foto.image_resized = True  # Marcar imagen como ya procesada
    foto.save()                # Guardar foto