import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "birthday/index.html", {
        "birthday": now.month == 7 and now.day == 13
    })