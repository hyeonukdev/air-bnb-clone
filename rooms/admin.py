from django.contrib import admin
from . import models

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    created = models.DateTimeField()
    updated = models.DateTimeField()