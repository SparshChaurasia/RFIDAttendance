from django.db import models

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
    StudName = models.CharField(max_length=255, null=True)
    StudClass = models.CharField(max_length=3, null=True)
    DateTime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        return super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        _n = self.Stud.Name
        _t = self.DateTime.strftime("%m/%d/%Y, %H:%M:%S")
        return f"{_n} {_t}"
