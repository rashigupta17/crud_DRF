from django.db import models
from django.conf import settings
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import uuid
from .managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin




    
class BaseModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class passengers(BaseModel):
    name = models.CharField(max_length = 200)
    contact = models.IntegerField()
    boardingid = models.IntegerField()
    #added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.ForeignKey('User', related_name='passengers', on_delete=models.CASCADE)
    highlighted = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Passengers'

def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.name)
    boardingid = 'table' if self.boardingid else False
    options = {'title': self.name} if self.name else {}
    formatter = HtmlFormatter(style=self.name, boardingid=boardingid,
                              full=True, **options)
    self.highlighted = highlight(self.contact, lexer, formatter)
    super(passengers, self).save(*args, **kwargs)


class User(BaseModel,AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=200,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique = True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    Pass = models.CharField(max_length=100)
    objects = UserManager()
    def __str__(self):
        return self.email

    # create objs for management
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'
