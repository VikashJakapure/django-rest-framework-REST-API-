from myapp.models import Stu
from rest_framework import serializers

class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stu
        fields = '__all__'