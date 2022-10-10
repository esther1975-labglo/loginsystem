from django.contrib import admin

from.models import registration

class reg(admin.ModelAdmin):
    list_display = ("id", "name", "age", "user_name", "password")
admin.site.register(registration, reg)
