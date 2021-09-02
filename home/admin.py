from django.contrib import admin
from .models import *

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catadmin)


class prodadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','img','stock']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,prodadmin)
# Register your models here.
