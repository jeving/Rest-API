from django.contrib import admin
from .models import Hospital

# Register your models here.
class MyApi(admin.ModelAdmin):
    list_display = ('id', 'Hospital', 'City', 'County')
    list_display_links = ('id', 'Hospital')
    search_fields = ('id', 'Hospital', 'City', 'County')
    list_per_page = 50

admin.site.register(Hospital,MyApi)