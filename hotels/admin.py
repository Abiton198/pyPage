from django.contrib import admin
from .models import Hotel


# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'name', 'location')


admin.site.register(Hotel, HotelAdmin)