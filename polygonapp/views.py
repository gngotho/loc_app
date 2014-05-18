from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.
from django.http import request
from .models import Region
from django.contrib.gis.geos import (Point, fromstr, fromfile, 
                GEOSGeometry, MultiPoint, MultiPolygon, Polygon)
import json

#def index(request):
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

	if request.method == 'POST':
		s = request.POST.get('data')
		print s
		d = json.loads(s)['overlays'][0]
		title = d['title']
		desc = d['content']
		print tuple(d['paths'][0])


		coords = request.POST
		#cord_list = []
		#for p in coords:
		#	print p[0]
		#	cord_list.append( GEOSGeometry('POINT(%s %s)' %(p[0], p[1])))
		#	print cord_list
	return render_to_response('test5.html', {},
                          context_instance=RequestContext(request))



def region(request):
	region  = Region.objects.all().order_by('-id')[0]

	return render_to_response('maps.html', {
        'obj': region,
    }, context_instance=RequestContext(request))