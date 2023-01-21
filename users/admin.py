from django.contrib import admin
from .models import UserPannel

class Panel(admin.ModelAdmin):
    list_display = ['owner','name','gender','phone','group','college','programe','level','topic','profile_pic','phone']

# Register your models here.
admin.site.register(UserPannel,Panel)