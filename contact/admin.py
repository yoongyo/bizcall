from django.contrib import admin
from .models import Contact, Item


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Item, ItemAdmin)