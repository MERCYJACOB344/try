from django.shortcuts import render
from rest_framework import viewsets
from .models import Question
from .serializers import EmployeeSerializer
class Employeeviewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = EmployeeSerializer


# Create your views here.
