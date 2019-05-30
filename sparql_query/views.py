from . queryyy import make_query
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json

def index(request):

	stringg = "Your query will be generated here...."
	if(request.GET.get('my_btn')):
		output_variable = "accident"
		city = request.GET.get('City')
		country = ""
		RunwaySurface = request.GET.get('Runway_SUrface')
		Aircraftmodel = request.GET.get('Aircraft_model')
		agee = "30"
		stringg = make_query(output_variable, city, country, RunwaySurface, Aircraftmodel, agee)

	return render(request, "sparql_query/index.html", {'stringg_abc' : mark_safe(stringg)})
