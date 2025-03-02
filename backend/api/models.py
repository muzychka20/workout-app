from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class PhysicalLevel(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'PhysicalLevel'
        verbose_name = 'PhysicalLevel'
        verbose_name_plural = 'PhysicalLevel'

    def __str__(self):
        return self.name


class Sex(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        db_table = 'Sex'
        verbose_name = 'Sex'
        verbose_name_plural = 'Sex'

    def __str__(self):
        return self.name


class BodyType(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'BodyType'
        verbose_name = 'BodyType'
        verbose_name_plural = 'BodyType'

    def __str__(self):
        return self.name


class Goal(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'Goal'
        verbose_name = 'Goal'
        verbose_name_plural = 'Goal'

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True, blank=False, null=False)

    username = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(
        max_length=100, unique=True, blank=False, null=False)

    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    goal = models.ForeignKey(
        Goal, blank=True, null=True, on_delete=models.SET_NULL)
    body_type = models.ForeignKey(
        BodyType, blank=True, null=True, on_delete=models.SET_NULL)
    sex = models.ForeignKey(Sex, blank=True, null=True,
                            on_delete=models.SET_NULL)
    physical_level = models.ForeignKey(
        PhysicalLevel, blank=True, null=True, on_delete=models.SET_NULL)

    registered_time = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    deleted = models.DateTimeField(blank=True, null=True)

    # for superadmin
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'User'

    def __str__(self):
        return f"{self.email} {self.username if self.username else ''}"


class Article(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    link = models.CharField(max_length=512, blank=False, null=False)

    class Meta:
        db_table = 'Article'
        verbose_name = 'Article'
        verbose_name_plural = 'Article'

    def __str__(self):
        return self.title


class TrainingType(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    duration_sec = models.IntegerField(blank=False, null=False)
    duration_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'TrainingType'
        verbose_name = 'TrainingType'
        verbose_name_plural = 'TrainingType'

    def __str__(self):
        return self.name


class Training(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False)
    training_type = models.ForeignKey(TrainingType, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Training'
        verbose_name = 'Training'
        verbose_name_plural = 'Training'

    def __str__(self):
        return self.training_type
