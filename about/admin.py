from django.contrib import admin
from .models import About


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'small_title', 'description')


admin.site.register(About, AboutAdmin)
# Register your models here.
