from django.db import models
from django.contrib.auth.models import AbstractUser
from userreg.validators import validate_bad_username, validate_username


SHORT_CHARFIELD = 50
MID_CHARFIELD = 150
LONG_CHARFIELD = 254
NAME_LEGNTH = 256
TEXT_SIZE = 15


class User(AbstractUser):
    username = models.CharField(
        blank=False,
        unique=True,
        max_length=MID_CHARFIELD,
        validators=[validate_bad_username, validate_username],
    )

    email = models.EmailField(
        max_length=LONG_CHARFIELD,
        unique=True,
        verbose_name='адрес электронной почты',
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ('username',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return self.username[:TEXT_SIZE]
