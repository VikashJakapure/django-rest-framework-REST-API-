from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.models import Emp
from authapp.serialzers import EmpSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


class Access(APIView):
    authentication_classes = ObtainAuthToken
    permission_classes = IsAuthenticated

    def get(self,request):
        data = Emp.objects.all()
        serialdata = EmpSerializer(data,many=True)
        return Response(serialdata.data)

    def post(self,request):
        data=request.data
        serialdata = EmpSerializer(data=data)
        if serialdata.is_valid():
            serialdata.save()
            return Response({'message':'data stored successfully'},status=200)
        else:
            return Response({'message': 'data is not valid'},status=404)


class Details(APIView):
    authentication_classes = ObtainAuthToken
    permission_classes = IsAuthenticated

    def get_obj(self,email):
        try:
            data = Emp.objects.get(email=email)
            return data
        except Exception as e:
            return Response({"message":"Provided email is not found in the database"})

    def get(self,request,email):
            data = self.get_obj(email)
            serialdata = EmpSerializer(data)
            return Response(serialdata.data)

    def put(self,request,email):
        info = request.data
        data = self.get_obj(email)
        serialdata = EmpSerializer(data,data=info,perticular=True)
        if serialdata.is_valid():
            serialdata.save()
            return Response({'message':'data is updated'},status=200)
        else:
            return Response({"error":"data is not valid"},status=404)

    def delete(self, request, email):
        data = self.get_obj(email)
        data.delete()
        return Response({"message": "data deleted successf  ully"}, status=200)
