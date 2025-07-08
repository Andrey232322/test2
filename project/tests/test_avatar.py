import pytest
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

from myapp.models import UserProfile


@pytest.mark.django_db
def test_avatar_is_square_after_upload():
    # Создаем прямоугольное изображение
    img = Image.new('RGB', (800, 600), color='blue')
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    buffer.seek(0)

    # Оборачиваем в Django-объект файла
    uploaded_file = SimpleUploadedFile('test.jpg', buffer.read(), content_type='image/jpeg')

    # Загружаем в модель
    user = UserProfile.objects.create(name='Test Square', avatar=uploaded_file)

    # Открываем результат из S3/MinIO
    user.avatar.open()
    result_img = Image.open(user.avatar)

    # Проверка квадратности
    width, height = result_img.size
    assert width == height, f"Image is not square: {width}x{height}"