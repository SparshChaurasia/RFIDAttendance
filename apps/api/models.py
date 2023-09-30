from django.db import models
from datetime import datetime, date

REPORTING_TIME = datetime.now().time().replace(hour=7, minute=30, second=0, microsecond=0)

class Classes(models.TextChoices):
    _9A = "9A"
    _9B = "9B"
    _10A = "10A"
    _10B = "10B"

class Status(models.TextChoices):
    _Late = "Late"
    _OnTime = "OnTime"

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


class Hardware(models.Model):
    HardwareID = models.AutoField(primary_key=True)
    HardwareName = models.TextField()

    def __str__(self):
        return self.HardwareName


class Entry(models.Model):
    Stud = models.ForeignKey(Student, models.CASCADE)
    StudName = models.CharField(max_length=255, null=True)
    StudClass = models.CharField(max_length=3, null=True)
    Hw = models.ForeignKey(Hardware, models.CASCADE)
    Date = models.DateField(auto_now_add=True, null=True) # Add a seprate date field for comparison and sorting
    Time = models.TimeField(auto_now_add=True, null=True) # Add a seprate time field for comparison and sorting
    Timestamp = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=10, choices=Status.choices, null=True)

    def save(self, *args, **kwargs):
        if datetime.now().time() > REPORTING_TIME:
            self.Status = Status._Late
        else:
            self.Status = Status._OnTime
        self.StudName = self.Stud.Name
        self.StudClass = self.Stud.Class
        return super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        _n = self.Stud.Name
        _t = self.Timestamp.strftime("%m/%d/%Y")
        return f"{_n} {_t}"
