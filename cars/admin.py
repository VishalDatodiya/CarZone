from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'photo'
    list_display = ('id','thumbnail','car_title','city','price','color','model','condition','year','is_featured')
    list_display_links = ('id','thumbnail','car_title')


    # is featured is edible from the outside
    list_editable = ('is_featured',)

    search_fields = ('id','car_title','color')
    list_filter = ('city','model','body_style','fuel_type')

admin.site.register(Car,CarAdmin)
