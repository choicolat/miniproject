from django.shortcuts import render


from .models import Lecture, Instructor, Student, Test 
from .serializers import InstructorsSerializer, LecturesSerializer, StudentsSerializer, TestsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def lectures_list(request):
    lectures = Lecture.objects.all()
    serializer = LecturesSerializer(lectures, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def instructors_list(request):
    instructors = Instructor.objects.all()
    serializer = InstructorsSerializer(instructors, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def students_list(request):
    students = Student.objects.all()
    serializer = StudentsSerializer(students, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def tests_list(request):
    tests = Test.objects.all()
    serializer = TestsSerializer(tests, many=True)
    return Response(serializer.data)


