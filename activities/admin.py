from django.contrib import admin
from .models import Activity


# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'small_title')


admin.site.register(Activity, ActivityAdmin)
# Register your models here.
