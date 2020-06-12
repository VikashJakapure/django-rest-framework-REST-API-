from django.shortcuts import render

# Create your views here.
from firstapp.models import Employee
from firstapp.serializers import EmployeeSerializer
from rest_framework import generics
from firstapp.pagination import MyPagination
class EmployeeAPIView(generics.ListAPIView):
    queryset =Employee.objects.all()
    serializer_class =EmployeeSerializer
    pagination_class =MyPagination
