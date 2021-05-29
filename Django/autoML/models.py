from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid

from .manager import MLUserManager # Импортируем созданный менеджер


class MLUser(AbstractBaseUser, PermissionsMixin):
    # Тут необходимо указать все поля , в соответствии с ERD диаграмой
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MLUserManager()

    def __str__(self):
        return self.email


class Dataset(models.Model):
    """
    Модель представляет данные, загруженные пользователем
    """
    STATUS_CHOICES = [
        (..., '...'),
    ]
    dataset_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    name = models.CharField('Name', null=False, max_length=20)
    user_id = models.ForeignKey('MLUser', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=...)
    description = models.TextField(max_length=100, help_text="Enter a brief description")
    message = models.TextField(max_length=100, help_text="message")
    cloud_storage = models.URLField(max_length=200)
    mapping = models.JSONField()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.dataset_id

    def create_dataset(self):
        """
        create dataset.
        """
        pass

    def import_file(self):
        pass

    def run_mapping(self):
        pass

    def check_data(self):
        pass
