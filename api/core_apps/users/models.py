import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _
from core_apps.users.managers import UserManager


class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Your username is not valid. A username should only contain letters , numbers, a dot "
        "@ Symbol, + symbol and a dash"
    )
    flags = 0


class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    username = models.CharField(
        _("Username"), max_length=50, unique=True, validators=[UsernameValidator]
    )

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()
    
    class Meta: 
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]
        
    @property
    def get_full_name(self): 
        return f"{self.first_name} {self.last_name}".strip()
    