from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        request.session["tasks"] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))
    return render(request, "tasks/add.html")