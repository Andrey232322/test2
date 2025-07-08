from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import UserProfile
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


@receiver(pre_save, sender=UserProfile)
def process_avatar(sender, instance, **kwargs):
    if instance.avatar and not hasattr(instance.avatar.file, 'processed'):
        try:
            img = Image.open(instance.avatar)
            img = img.convert('RGB')

            # Обрезка до квадрата
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            img = img.crop((left, top, right, bottom))

            # Сжатие изображения
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85)
            buffer.seek(0)

            # Заменяем оригинальный файл обработанным
            file_name = instance.avatar.name.rsplit('/', 1)[-1]
            instance.avatar.save(file_name, ContentFile(buffer.read()), save=False)

            # Флаг, чтобы избежать повторной обработки
            instance.avatar.file.processed = True

        except Exception as e:
            print(f'Ошибка обработки изображения: {e}')