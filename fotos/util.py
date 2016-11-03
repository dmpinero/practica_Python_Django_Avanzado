from easy_thumbnails.files import generate_all_aliases


def generate_responsive_images(foto):
    generate_all_aliases(foto.image, True)