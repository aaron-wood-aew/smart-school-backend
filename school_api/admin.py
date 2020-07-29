from django.contrib import admin
from .models import CustomUser, Student, Teacher, Address, Classroom, Account

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = CustomUser

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Address)
admin.site.register(Classroom)
admin.site.register(Account)