from rest_framework.viewsets import ModelViewSet

from users_app.models import User
from users_app.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
