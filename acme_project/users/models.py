from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField('Биография', max_length=255, null=True)

    class Meta:
        verbose_name = 'Расширение Пользователя'

    def __str__(self):
        return str(self.user)
