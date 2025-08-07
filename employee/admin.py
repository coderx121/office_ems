from django.contrib import admin
from .models import EmployeeProfile, Attendance, Task

admin.site.register(EmployeeProfile)
admin.site.register(Attendance)
admin.site.register(Task)