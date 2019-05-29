from django.shortcuts import render

# Create your views here.


def index(request):

	print ("hello")
	# if(request.GET.get('my_btn')):
	# 	print ("chal rha...")
	stringg = "full of stars...."
	# print (request.GET.get('AircraftModel_ID').value)
	return render(request, "sparql_query/index.html", {'stringg' : stringg})
