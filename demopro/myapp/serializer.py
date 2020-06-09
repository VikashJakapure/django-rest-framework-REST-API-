from myapp.models import Student
from rest_framework.serializers import ModelSerializer

class StudentSerilizer(ModelSerializer):

    class Meta():

        model = Student
        fields = '__all__'


