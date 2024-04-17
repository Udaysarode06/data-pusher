from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, account_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not account_name:
            raise ValueError("Users must have an account name")

        user = self.model(
            email=self.normalize_email(email),
            account_name=account_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, account_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            account_name=account_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=100, unique=True)
    account_name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    app_secret_token = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['account_name']

    # Add related names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='account_set',
        related_query_name='account',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='account_set',
        related_query_name='account',
    )

    def __str__(self):
        return self.account_name
class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

    def __str__(self):
        return f"{self.account.account_name} - {self.url}"