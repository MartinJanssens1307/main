from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    name="Martin"
    return render(request, "FirstApp/index.html", {"name":name})

def hello(request):
    return HttpResponse("Hello, world")