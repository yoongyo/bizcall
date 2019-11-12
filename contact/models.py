from django.db import models
from django.conf import settings


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Item(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.name
