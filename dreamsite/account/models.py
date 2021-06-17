from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, sex, nationality, password=None):
        #Creates and saves a User
        if not email:
            raise ValueError('Please provide an email address.')
        if not username:
            raise ValueError('Please create a username.')
        if not date_of_birth:
            raise ValueError('Please provide your date of birth.')
        if not nationality:
            raise ValueError('Please provide your nationality.')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            sex=sex,
            date_of_birth=date_of_birth,
            nationality=nationality,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, sex, date_of_birth, nationality, password=None):
        #Creates and saves a superuser
        user = self.create_user(
                email,
                username=username,
                sex=sex,
                date_of_birth=date_of_birth,
                nationality=nationality,
            )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    SEX_CHOICES = [
    ('', '------'),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ]

    email = models.EmailField(verbose_name='email address', max_length=60, unique=True)
    username = models.CharField(max_length=25, unique=True)
    date_of_birth = models.DateField(verbose_name='date of birth')
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    nationality = CountryField(blank_label='(select country)')
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now=True)
    number_of_posts = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth', 'sex', 'nationality']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        #Does the user have permissions to view the app `app_label`?"
        return True
