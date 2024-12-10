from rest_framework import serializers
from api.submodels.models_login import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age']
