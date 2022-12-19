from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def request(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method!") 
    
    uid = request.POST.get("uid")
    print(uid)
    return HttpResponse(uid)    
