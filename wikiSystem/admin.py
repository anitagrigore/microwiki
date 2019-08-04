from django.contrib import admin
from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Pages, PagesAdmin)
