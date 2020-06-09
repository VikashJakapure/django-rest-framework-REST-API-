from django.contrib import admin
from myapp.models import Student
from django.contrib.admin import ModelAdmin


class StudentAdmin(ModelAdmin):

    class Meta():
        model = Student
        fields = '__all__'

admin.site.register(Student,StudentAdmin)
