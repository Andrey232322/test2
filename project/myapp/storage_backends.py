from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class MinioStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = None

    def __init__(self, *args, **kwargs):
        kwargs['endpoint_url'] = settings.AWS_S3_ENDPOINT_URL
        super().__init__(*args, **kwargs)