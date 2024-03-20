from rest_framework import serializers
from .models import Lecture
from .models import Instructor
from .models import Student
from .models import Test

class LecturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = '__all__'

class InstructorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Instructor
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
       

class TestsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = '__all__'