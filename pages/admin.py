from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbNail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%"  />'.format(object.photo.url))



    # short description of thumbNail which will show at admin site
    thumbNail.short_description = 'photo'




    list_display = ('id','thumbNail','first_name','last_name','designation','created_date')

    # we have to write the same variable/list name as it is
    # this all are the clicable links
    list_display_links = ('id','thumbNail','first_name')



    # Search field
    search_fields = ('id','first_name','designation')

    # filter the team member by their designation
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)
