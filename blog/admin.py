from django.contrib import admin

# Register your models here.
from .models import post

class postAdmin(admin.ModelAdmin):
    readonly_fields=['slug', 'publish', 'update']

admin.site.register(post, postAdmin)