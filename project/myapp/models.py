from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.storage_backends import MinioStorage

minio_storage = MinioStorage()

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, storage=minio_storage)

