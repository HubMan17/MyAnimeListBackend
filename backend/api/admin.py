from django.contrib import admin

from .models import Directoranime

# Register your models here.
class DirectoranimeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    
    def __str__(self):
        return self.name

admin.site.register(Directoranime, DirectoranimeAdmin)