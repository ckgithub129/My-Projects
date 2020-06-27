from django.contrib import admin

# Register your models here.

from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display=['title','completed','created_at']

admin.site.register(Task,TaskAdmin)


