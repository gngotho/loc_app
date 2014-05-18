#from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from . import models

class RegionAdmin(admin.GeoModelAdmin):
	search_fields = ['name']
	list_display = ['name']

admin.site.register(models.Region, RegionAdmin)