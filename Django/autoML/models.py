from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Импортируем созданный менеджер
from .manager import MLUserManager


# class User(AbstractBaseUser, PermissionsMixin):
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    # defaultDatasetForMapping = models.JSONField()
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MLUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Dataset(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование набора')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    status = models.CharField(max_length=30, verbose_name='Статус')
    description = models.CharField(max_length=500, verbose_name='Описание данных', blank=True)
    message = models.TextField(verbose_name='Сообщения')
    # cloud_storage_location_dataset = models.JSONField()
    # mapping = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Набор данных')
        verbose_name_plural = _('Наборы данных')


class Project(models.Model):
    project_name = models.CharField(max_length=50, unique=True, verbose_name='Наименование проекта')
    project_type = models.CharField(max_length=50, verbose_name='Тип проекта')
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # project_parameters_default = models.JSONField()

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')


class ProjectResults(models.Model):
    result_name = models.CharField(max_length=100, unique=True, verbose_name='Результат')
    dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT, verbose_name='Наименование набора')
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='Наименование проекта')
    # project_parameters = models.JSONField()
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # cloud_storage_result_location_project = models.JSONField()
    # cloud_storage_result_location_project_public = models.JSONField()
    status = models.CharField(max_length=50, verbose_name='Статус')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.result_name

    class Meta:
        verbose_name = _('Результат')
        verbose_name_plural = _('Результаты')
