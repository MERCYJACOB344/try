from rest_framework import serializers
from .models import Question
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'
