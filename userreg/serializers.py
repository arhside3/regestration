from djoser.serializers import UserCreateSerializer, UserSerializer
from userreg.models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'id',
            'first_name',
            'last_name',
            'password',
        )
        model = User


class ReadUserSerializer(UserSerializer):
    class Meta:
        fields = (
            'username',
            'id',
            'first_name',
            'last_name',
        )
        model = User
