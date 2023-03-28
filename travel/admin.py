from django.contrib import admin
from .models import Travel


# Register your models here.
class TravelAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'title', 'description')


admin.site.register(Travel, TravelAdmin)
