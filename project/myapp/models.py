from django.db import models

from myapp.storage_backends import MinioStorage

minio_storage = MinioStorage()
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, storage=minio_storage)

    # def save(self, *args, **kwargs):
    #     print('Storage:', self.avatar.storage.__class__)
    #     super().save(*args, **kwargs)