from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from shop.models import Service, Product, Support
from conf import choices
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return f"/users/{self.pk}/"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    gold_member = models.BooleanField(default=False, blank=True)
    city = models.CharField(max_length=200, default="", blank=True)
    country = models.CharField(max_length=200, default="", blank=True)
    product_list = models.ManyToManyField(
        Product, related_name='product_lists', blank=True)
    service_list = models.ManyToManyField(
        Service, related_name='service_lists', blank=True)
    support_list = models.ManyToManyField(
        Support, related_name='support_lists', blank=True)
    conversion_rate = models.IntegerField(default=0, blank=True)
    occupation = models.CharField(
        max_length=20, choices=choices.PROFILE_CHOICES, default='Normal User', blank=True)
    gender = models.CharField(
        max_length=6, choices=choices.GENDER_CHOICES, default='Male', blank=True)

    def __str__(self):
        return f"{self.user.email} {str(self.birthday)} {self.city } {self.country} Gold Member: {str(self.gold_member)}"


class InAppSearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.product)
