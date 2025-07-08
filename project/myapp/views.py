from rest_framework import viewsets


from myapp.models import UserProfile
from myapp.serializer import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
