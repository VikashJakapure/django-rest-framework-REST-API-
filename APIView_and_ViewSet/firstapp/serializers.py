# To converting json to python(dict) we required serializers
from rest_framework import serializers

class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
     
