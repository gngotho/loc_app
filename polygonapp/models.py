#from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Region(models.Model):
	name = models.CharField(max_length=100)

	mpolygon = models.PolygonField('polygons', null=True, blank=True, spatial_index=False)
	objects = models.GeoManager()

	def __str__(self):
		return self.name

	#cordinate = models.CharField(max_length=100)


