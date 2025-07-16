from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, UserView

profiles = DefaultRouter()
user = DefaultRouter()
profiles.register(r'profiles', UserProfileViewSet, basename='profile')
user.register(r'user', UserView, basename='user')

urlpatterns = [
    path('', include(profiles.urls)),
    path('', include(user.urls)),
]