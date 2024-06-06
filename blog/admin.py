from django.contrib import admin

# Register your models here.
from .models import post

class postAdmin(admin.ModelAdmin):
    readonly_fields=['slug']

admin.site.register(post, postAdmin)