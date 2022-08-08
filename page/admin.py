from turtle import width
from django.contrib import admin
from page.models import Team
from django.utils.html import format_html
# Register your models here.

class adminsite(admin.ModelAdmin,):
    def Photo(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.image.url))
    Photo.short_description = 'Images'
    search_fields = ('firstname','description',)
    list_filter= ('firstname','description',)
    list_display= ('firstname','last_name','Photo','description','facebook','twitter','google')
admin.site.register(Team,adminsite)

