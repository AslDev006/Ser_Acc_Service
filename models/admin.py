from django.contrib import admin
from .models import *
@admin.register(Contact_Model)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'called', 'create_time']
    list_editable = ['called']
    ordering = ['-create_time']