from django.contrib import admin
from .models import Contact, Item


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Item, ItemAdmin)