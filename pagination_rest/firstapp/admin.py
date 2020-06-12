from django.contrib import admin

# Register your models here.
from django.contrib import admin
from firstapp.models import Employee
# # Register your models here.
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display=['id','eno','ename','esal','eaddr']
admin.site.register(Employee)