from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    eduction = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.phone)  + str(self.address)