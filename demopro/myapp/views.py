import os
import uuid
from django.shortcuts import render
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student
from myapp.serializer import StudentSerilizer
from rest_framework.viewsets import ViewSet,ModelViewSet
from gtts import gTTS
from rest_framework import status


class Details(APIView):

    def get(self,request,pk=None):

        if pk:
            model_data = Student.objects.get(id=pk)
            serilizer = StudentSerilizer(model_data,many=False)
            print(serilizer.data)
            return Response(serilizer.data,status=status.HTTP_200_OK)

        else:
            model_data = Student.objects.all()
            serilizer = StudentSerilizer(model_data,many=True)
            return Response(serilizer.data)

    def post(self,request):
        data = request.data
        srilizer = StudentSerilizer(data=data)
        if srilizer.is_valid():
            srilizer.save()
            return Response(srilizer.data,status=status.HTTP_201_CREATED)
        else:
            return Response("data is not valid")

    def put(self,request,pk):

        model_data = Student.objects.get(id=pk)
        request_data = request.data
        serilizer = StudentSerilizer(instance=model_data,data=request_data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response('data is not valid')



    def delete(self,request,pk):
        model_data = Student.objects.get(id=pk)
        model_data.delete()
        return Response("data is deleted")







class ConvertView(APIView):

       def post(self,request):
           text = request.data['text']
           self.convert(text,'en')
           file = open('welcome.mp3','rb')
           return FileResponse(file)

       def convert(self,text,ln):
            myobj = gTTS(text=text, lang=ln, slow=False)
            myobj = ('welcome.mp3')
            return True

















            # def post(self,request):
    #     serilizer = StudentSerilizer(data=request.data)
    #     if serilizer.is_valid():
    #         serilizer.save()
    #         return Response(serilizer.data)
    #     else:
    #         return Response("invalid data")
    #
    #
    # def put(self,request,pk):
    #     model_data = Student.objects.get(id=pk)
    #     serilizer = StudentSerilizer(instance=model_data,data=request.data)
    #     if serilizer.is_valid():
    #         serilizer.save()
    #         return Response(serilizer.data)
    #     else:
    #         return Response("invalid data")


    # def delete(self,request,pk):
    #     data = Student.objects.get(id=pk)
    #     serial = StudentSerilizer(data)
    #
    #     data.delete()
    #     return Response("data is deleted")


class TextToAudio(APIView):

    def post(self,request):
        text = request.data['text']
        self.convert(text)
        file = open('welcome.mp3','rb')
        response = FileResponse(file)
        return response

    def convert(self,text):
        myobj = gTTS(text=text, lang='en', slow=False)
        myobj.save("welcome.mp3")
        return True






        #  curl -X PUT  http://127.0.0.1:8000/myapp/delete/4/ -d 'name=sanchit kumar&course_id=36&address=nashik'





# class TestViewSet(ViewSet):
#
#     def list(self,request):
#         query = Student.objects.all()
#         serializer = StudentSerilizer(query,many=True)
#         return Response(serializer.data)
#
#     def retrieve(self,request,pk):
#         query = Student.objects.get(id=pk)
#         serializer = StudentSerilizer(query)
#         return Response(serializer.data)





# class TestViewSet(ModelViewSet):
#     serializer_class = StudentSerilizer
#     queryset = Student.objects.all()

