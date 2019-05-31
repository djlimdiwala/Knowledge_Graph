from . query_maker import make_query
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json

def index(request):

	stringg = "Your query will be generated here...."
	if(request.GET.get('my_btn')):
		output_variable = "accident"

		city = request.GET.get('City').replace(" ", "")
		RunwaySurface = request.GET.get('Runway_Surface').replace(" ", "")
		pilot_certi = str(request.GET.get('pilot_certificate')).replace(" ", "")
		Aircraft_manufacturer = str(request.GET.get('aircraft_manufacturer')).replace(" ", "")
		Engine_manufacturer = str(request.GET.get('engine_manufacturer')).replace(" ", "")

		pilot_age_min =  str(request.GET.get('Pilot_age_min')).replace(" ", "")
		pilot_age_max =  str(request.GET.get('Pilot_age_max')).replace(" ", "")
		agee = "30"
		Aircraftmodel = ""
		country = ""

		# print (Engine_manufacturer)
		# print ("here")
		stringg = make_query(output_variable, str(city), country, str(RunwaySurface), Aircraftmodel, pilot_age_min, pilot_age_max, pilot_certi, Aircraft_manufacturer, Engine_manufacturer)

	return render(request, "sparql_query/index.html", {'stringg_abc' : mark_safe(stringg)})
