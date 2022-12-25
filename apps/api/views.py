from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
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

    entry = Entry(Stud=stud)
    entry.save()

    return HttpResponse(200)    

@csrf_exempt
def r_list(request):
    """
    req params: class, sortby
    """
    if request.method != "POST":
        return HttpResponse("Invalid request method!") 

    entry = Entry.objects.all()
    entry_json = serializers.serialize("json", entry)
    # print("from api", entry)

    return HttpResponse(entry_json, content_type='application/json')
