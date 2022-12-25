from django.urls import path
from . import views

urlpatterns = [
    path("new", views.r_new),
    path("list", views.r_list)
]
