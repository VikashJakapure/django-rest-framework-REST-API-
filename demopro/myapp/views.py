from rest_framework.views import APIView
from django.http.response import FileResponse
from rest_framework.response import Response
from myapp.models import Student
from myapp.serializer import StudentSerilizer
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class QueryParams(APIView):

    def get(self,request):
        data = request.query_params
        print(data['abc'])
        print(data['pi'])
        return Response('done')

class StudentGenericViewSet(GenericAPIView,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):

    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentSerilizer

    def get(self, request,pk=None):
        if pk:
            return self.retrieve(request)
        else:
          return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)































