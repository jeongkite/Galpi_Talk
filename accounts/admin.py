from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(AccessCode)
class AccessCodeAdmin(admin.ModelAdmin):
    list_display = ['access_code', 'user']
    list_display_links = ['access_code', 'user']
    search_fields = ['user__username']


@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'birth']
    list_display_links = ['user', 'name', 'birth']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'is_other']
    list_display_links = ['user', 'name']
    search_fields = ['user__username']
