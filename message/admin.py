from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']


admin.site.register(Message, MessageAdmin)
