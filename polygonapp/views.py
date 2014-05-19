from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.
from django.http import request
from .models import Region
from django.contrib.gis.geos import (Point, fromstr, fromfile, 
                GEOSGeometry, MultiPoint, MultiPolygon, Polygon)
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	'''
	Here we'll get the points from the user input, and store them
	in a PolygonField. Also, title and description of the polygon
	'''
	if request.method == 'POST':
		s = request.POST.get('data')
		d = json.loads(s)['overlays'][0]
		title = d['title']
		desc = d['content']
		c = d['paths'][0]#here we get the key-value pair of lat/long of all the points
		cord_list = []
		coords = [[v for k, v in d.iteritems() ] for d in c]#remove the keys from the dict, make it a nested list

		if coords[0] != coords[-1]:#if it's not a linear ring, force it---> mischevous, sorry.
			coords.append(coords[0])
		for p in coords:
			cord_list.append(GEOSGeometry('POINT(%s %s)' %(p[0], p[1])))
		p = Polygon(cord_list)
		region_obj = Region(name=title, mpolygon=p)
		region_obj.save()

		return region(request)
	return render_to_response('draw.html', {},
                          context_instance=RequestContext(request))



def region(request):
	pol_obj = Region.objects.all().order_by('-id')[0]
	geojson = pol_obj.mpolygon.geojson
	coords =  pol_obj.mpolygon.coords[0]
	centre =  pol_obj.mpolygon.centroid.coords
	return render_to_response('maps.html', 
		{'geojson': geojson,'coords':coords, 'centroid': centre, }, context_instance=RequestContext(request))