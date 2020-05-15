from django.db import models
from django.conf import settings
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class boardingpass(models.Model):
    flightdate = models.DateTimeField()
    id = models.IntegerField(primary_key =True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    

class passengers(models.Model):
    name = models.CharField(max_length = 200)
    contact = models.IntegerField()
    boardingid = models.ForeignKey(boardingpass, on_delete=models.CASCADE)
    #added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='passengers', on_delete=models.CASCADE)
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