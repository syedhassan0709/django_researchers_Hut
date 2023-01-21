from django.contrib import admin
from Publications.models import Publication
from Publications.models import Year,Field

# Register your models here.


class AdminPublication(admin.ModelAdmin):
    
    list_display = ['year','level','title','author','text']


admin.site.register(Publication,AdminPublication)
admin.site.register(Year)
admin.site.register(Field)