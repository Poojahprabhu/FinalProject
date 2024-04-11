from django.contrib import admin

# Register your models here.

from .models import user, feedback
admin.site.register(user)
admin.site.register(feedback)
