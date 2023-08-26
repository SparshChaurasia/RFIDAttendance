from django.contrib import admin
from .models import Student, Entry, Hardware

admin.site.register(Student)
admin.site.register(Hardware)
admin.site.register(Entry)
