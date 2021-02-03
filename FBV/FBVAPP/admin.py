from django.contrib import admin
from FBVAPP.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    l=["eno","ename","esal","eaddr"]
admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
