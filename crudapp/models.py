from django.db import models
from django.conf import settings
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
import uuid


class passengers(models.Model):
    name = models.CharField(max_length = 200)
    contact = models.IntegerField()
    boardingid = models.IntegerField()
    #added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #owner = models.ForeignKey('settings.AUTH_USER_MODEL', related_name='passengers', on_delete=models.CASCADE)
    highlighted = models.TextField()
    def __str__(self):
        return self.name

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

class User(AbstractBaseUser, PermissionsMixin):
    _id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(max_length=150,unique=True)
    firstname = models.CharField(max_length=100,null=True,blank=True)
    surname = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=255)
    Pass = models.CharField(max_length=255, null = True, blank=True)    
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    is_superuser = models.BooleanField(default=False)



    
    def __str__(self):
        return self.email
    USERNAME_FIELD = 'email'
    class Meta:
        db_table= 'user'
