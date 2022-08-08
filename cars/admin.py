from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarsSection(admin.ModelAdmin):
    def Photo(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.car_photo.url))
    # Photo.short_description = 'Car Images'
    list_display = ('title', 'Photo','city', 'year', 'is_featured')
    search_fields = ('title','year',)
    list_filter= ('title','year',)
    list_editable = ('is_featured',)

admin.site.register(Car,CarsSection)