from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class ViDuView(APIView):
    def get(self, request):
        return Response({'vidu': 'Xin chao cac ban'})


class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
