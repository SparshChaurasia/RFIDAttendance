from django.shortcuts import render, HttpResponse
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
    print("from api", entry)
    return HttpResponse(entry) 
