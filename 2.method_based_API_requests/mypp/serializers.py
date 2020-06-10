from rest_framework import serializers
from mypp.models import Emp


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'