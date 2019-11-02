from django.contrib import admin
from .models import News, Updates
from tinymce.widgets import TinyMCE
from django.db import models
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ['title', 'published']}),
        ('Content', {"fields": ['content']})
    ]

    formfield_overrides = {
        models.TextField:{'widget': TinyMCE()}
    }

class UpdatesAdmin(admin.ModelAdmin):
    fieldsets_updates = [
        ("Title/date", {"fields": ['title', 'published']}),
        ('Content', {"fields": ['content']})
    ]

    formfield_overrides = {
        models.TextField:{'widget': TinyMCE()}
    }
admin.site.register(News, PostAdmin)
admin.site.register(Updates, UpdatesAdmin)
# Register your models here.
