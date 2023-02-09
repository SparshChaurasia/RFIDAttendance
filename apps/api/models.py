from django.db import models
from datetime import date, datetime

class Classes(models.TextChoices):
    _9A = "9A"
    _9B = "9B"
    _10A = "10A"
    _10B = "10B"

class Student(models.Model):
    UID = models.CharField(max_length=12, primary_key=True)
    Name = models.CharField(max_length=255)
    Class = models.CharField(max_length=3, choices=Classes.choices)

    def save(self, *args, **kwargs):
        self.Name = self.Name.lower()
        self.UID = self.UID.upper()
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.Name

class Entry(models.Model):
    Stud = models.ForeignKey(Student, models.CASCADE)
    StudName = models.CharField(max_length=255, null=True) # Split name and class field for json serialization
    StudClass = models.CharField(max_length=3, null=True)
    Date = models.DateField(date.today(), null=True) # Split date and time field for json serialization
    Time = models.TimeField(datetime.now().time(), null=True)

    def save(self, *args, **kwargs):
        return super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        _n = self.Stud.Name
        _t = self.Date.strftime("%m/%d/%Y")
        return f"{_n} {_t}"
