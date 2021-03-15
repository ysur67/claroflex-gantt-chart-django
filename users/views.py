from django.contrib.auth import get_user_model
from rest_framework import viewsets

from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.filter(is_active=True)
    serializer_class = UserSerializer
