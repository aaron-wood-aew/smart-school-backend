from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = (models.CharField(max_length=100, blank=False))
    last_name = (models.CharField(max_length=100, blank=False))
    is_teacher = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=True)

    def __str__(self):
        return (f'{self.id} {self.first_name} {self.last_name}')

class Student(models.Model):
    guardian_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

class Teacher(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    rate = models.CharField(max_length=200)

    def __str__(self):
        return (f'{self.user_id.first_name} {self.user_id.last_name}')

class Address(models.Model):
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return (f'{self.street_1} {self.street_2} {self.city}, {self.state}  {self.zip_code}')

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    is_full = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Account(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card = models.CharField(max_length=16)