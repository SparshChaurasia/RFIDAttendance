from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

@login_required(login_url="/login")
def dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url="/login")
def records(request):
    return render(request, "records.html")

@login_required(login_url="/login")
def attendance(request):
    return render(request, "attendance.html")
