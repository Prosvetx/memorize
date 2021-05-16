import os
import uuid
from config.settings import BASE_DIR
from django.utils.encoding import force_text


def image_name_path_generator(instance, filename):
    extension = filename.split('.')[-1]
    path_in_media = 'images'
    filename = force_text(uuid.uuid4())[20:] + f'.{extension}'

    path = os.path.join(path_in_media, filename)
    check_path = BASE_DIR / 'media' / os.path.join(path_in_media, filename)

    if os.path.exists(check_path):
        return image_name_path_generator(instance, filename)
    return path