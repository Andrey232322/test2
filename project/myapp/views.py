from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from myapp.models import UserProfile, User
from myapp.serializer import UserProfileSerializer, UserSerializer
from myapp.permissions import IsOwner
from rest_framework import viewsets, status
from rest_framework.response import Response

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def create(self, request, *args, **kwargs):
        if hasattr(request.user, 'userprofile'):
            return Response(
                {"error": "Профиль уже существует для этого пользователя"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_profile(self, request, pk=None):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
