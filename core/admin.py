from django.contrib import admin
from .models import User
# Register your models here.
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin
class DisplayUser(UserAdmin):
    add_fieldsets = (
        (None,{
            'classes' : ('wide,'),
            'fields' : ['username','email','password1','password2']
        }),
    )


admin.site.register(get_user_model(),DisplayUser)    