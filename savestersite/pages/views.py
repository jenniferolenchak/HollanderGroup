from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Haha fuck u</h1>")
    return render(request, "home.html", {})