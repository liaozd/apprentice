from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import viewsets

from tutorial.quickstart.serializers import GroupSerializer
from tutorial.quickstart.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
