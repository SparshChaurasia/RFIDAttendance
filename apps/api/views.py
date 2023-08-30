from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from .models import Student, Entry


@csrf_exempt
def r_new(request):
    """
    req params: uid
    """
    if request.method != "POST":
        return HttpResponse("Invalid request method!") 
    
    uid = request.POST.get("uid")
    stud = Student.objects.get(UID=uid)

    entry = Entry(Stud=stud, StudName=stud.Name, StudClass=stud.Class)
    entry.save()

    return HttpResponse(200)    


def r_list(request):
    """
    req params: class, sortby
    """
    if request.method != "POST":
        return HttpResponse("Invalid request method!") 

    date = request.POST.get("date")
    s_class = request.POST.get("class")
    sort_by = request.POST.get("sort")

    # print(date, sort_by, s_class)
    
    entry = Entry.objects.all()
    if date != "":
        date_obj = datetime.strptime(date, f"%Y-%m-%d").date()
        entry = entry.filter(Date=date_obj)
    else:
        entry = entry.filter(Date=datetime.now().date())
    if s_class != "all":
        entry = entry.filter(StudClass=s_class)

    if sort_by == "time":
        entry = entry.order_by("Timestamp").values()
    elif sort_by == "alphabetically":
        entry = entry.order_by("StudName").values()
    print(entry)

    return render(request, "attendance.html", {"entries":entry})
