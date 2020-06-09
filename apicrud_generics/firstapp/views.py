from django.shortcuts import render
from firstapp.models import Employee
from firstapp.serializers import EmployeeSerializer
from rest_framework import generics
#from rest_framework import ListCreateAPIView
# Create your views here.
class EmployeeListCreateApi(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id' 
