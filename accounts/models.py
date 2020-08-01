from django.db import models


# Create your models here.


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=66)
    nickname = models.CharField(max_length=25, unique=True, default=login)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}'

    def profiles_list(self):
        pass
