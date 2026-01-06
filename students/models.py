from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name