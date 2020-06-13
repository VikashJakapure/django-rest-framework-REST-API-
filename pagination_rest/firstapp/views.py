from django.shortcuts import render

# Create your views here.
from firstapp.models import Employee
from firstapp.serializers import EmployeeSerializer
from rest_framework import generics
from firstapp.pagination import MyPagination
class EmployeeAPIView(generics.ListAPIView):
    # queryset =Employee.objects.all()
    serializer_class =EmployeeSerializer
    # pagination_class =MyPagination
    #DRF Filtering
    # search_fields = ('ename', 'eno') # DRF filtering
    # search_fields = ('eno',)
    # search_fields = ('^eno',)
    search_fields = ('^eno',)  #exactly equal to eno.
    ordering_fields = ('eno', 'esal')
    #http: // 127.0.0.1: 8000 / api /?mysearch = 2
    # It returns all Employee records where eno contains '2'

#vanilla filter
    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('ename')
        if name is not None:
            qs = qs.filter(ename__icontains=name)
        return qs

        #http://127.0.0.1:8000/api?ename=John
