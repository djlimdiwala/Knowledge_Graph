from urllib.parse import quote
from urllib.request import urlopen
import requests
import json
import csv


def make_query (print_variable, city, country, RunwaySurface, Aircraftmodel, agee):


	city1 = "?city"
	country1 = "?country"
	RunwaySurface1 = "?RunwaySurface"
	Aircraftmodel1 = "?Aircraftmodel"
	Aircraft1 = "?Aircraft"
	pilot1 = "?pilot"
	print_variable1 = "?accident"
	Prefix_1 = "PREFIX aircraftaccident: <https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl#> "
	Prefix_2 = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "

	

	if city != "":
		city1 = "aircraftaccident:" + city

	if country != "":
		country1 = "aircraftaccident:" + country

	if RunwaySurface != "":
		RunwaySurface1 = "aircraftaccident:" + RunwaySurface
	
	if Aircraftmodel != "":
		Aircraftmodel1 = "aircraftaccident:" + Aircraftmodel


	Sparql_Query = "SELECT ?" + print_variable + " WHERE { "

	Sparql_Query = Sparql_Query + "?accident aircraftaccident:occurredAtCity " + city1 + " . "                            + "?accident aircraftaccident:occurredAtCountry " + country1 + " . "                                         + "?accident aircraftaccident:hasAircraft " + Aircraft1 + " . "                                                          + "?accident aircraftaccident:hasPilot " + pilot1 + " . "                                                                           + pilot1 + " aircraftaccident:hasAge ?Age . "                                                                                      + "?accident aircraftaccident:hasRunwaySurfaceType " + RunwaySurface1 + " . "

   # + "FILTER( ?Age >= " + agee + " && ?Age <= " + agee + " ) .
                                                   # + "?Aircraft hasAircraftModel " + Aircraftmodel1 + " . "
	Sparql_Query = Prefix_1 + " " + Prefix_2 + " " + Sparql_Query + "}"


	headers = {'Accept':'application/json'}
	Sparql_Query = requests.get("http://10.130.167.218:3030/Accident_2/?query=" + quote(Sparql_Query), headers=headers).text
	# Sparql_Query = json.loads(Sparql_Query)

	result = json.loads(Sparql_Query.replace('\'','"'))
	accident_number = []
	out = "";

	print(result)

	for i in range(len(result['results']['bindings'])):
		accident_number.append(result['results']['bindings'][i]['accident']['value'].split("#")[1]);
		# out += result.bindings[i].accident.value.split("#")[1].split("_")[1] + "\n"; 
	


	text = "<ul>";
	for i in range(len(result['results']['bindings'])):
		text += "<li>" + accident_number[i] + "</li>";
	
	text += "</ul>";


	return text
	
