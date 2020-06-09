from django.contrib import admin
from firstapp.models import Employee
# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']


admin.site.register(Employee,Employeeadmin)
