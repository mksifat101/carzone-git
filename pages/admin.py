from django.contrib import admin
from .models import My_Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    thumbnail.short_description = "Photo"

    list_display = ('id', 'thumbnail', 'first_name', 'degination', 'create_date')
    list_display_links = ('id', 'thumbnail', 'first_name')

admin.site.register(My_Team, TeamAdmin)
