from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Entry

@csrf_exempt
def request(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method!") 
    
    uid = request.POST.get("uid")
    stud = Student.objects.get(UID=uid)

    entry = Entry(Stud=stud)
    entry.save()

    return HttpResponse(200)    
