from django.contrib import admin
from .models import passengers,User
class UserAdmin(admin.ModelAdmin):
    list_display  = ['_id','email','username','contact']

admin.site.register(passengers)
admin.site.register(User,UserAdmin)