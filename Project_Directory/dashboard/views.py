from django.shortcuts import render, HttpResponse

# Create your views here.
#def dashboard(request):
#	return HttpResponse("Dashboard")


def dashboard(request):
	return render(request, 'DashboardTemplates/dashboard.html')