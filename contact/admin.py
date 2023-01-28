from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'car_title', 'city', 'email', 'created_date')
    list_display_links = ('id', 'firstname')
    search_fields = ('firstname','lastname','email','car_title')
    list_per_page = 25

admin.site.register(Contact,ContactAdmin)
