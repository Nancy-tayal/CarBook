from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,email,name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name, **extra_fields)
        print(email)
        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,name, password, **extra_fields):
        """
        Create and save a Superuser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser = True")
        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser must have is_admin = True")
        return self.create_user(email,name, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True,max_length=255)
    password = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    phone =PhoneNumberField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','name','phone']
    class Meta:
        app_label = "accounts"
        db_table = "user"
    
    def __str__(self):
        return str(self.email)

    @property
    def get_full_name(self):
        return f'{self.name}'
    
    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return self.is_staff
