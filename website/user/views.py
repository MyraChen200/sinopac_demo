from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from user.serializers import UserSerializer
from django.contrib.auth import get_user_model
from user.models import User
# User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer