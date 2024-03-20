from django.db import models

# Create your models here.
class Lecture(models.Model):
    lecture_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lecture_satisfaction = models.CharField(max_length=100)
    content = models.TextField()
    textbook= models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)

    
class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class Instructor(models.Model):
    grade = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    question_answer_rate = models.CharField(max_length=100)
   


class Test(models.Model):
    student_id = models.CharField(max_length=100)
    lecture_id = models.CharField(max_length=100)
    started_at = models.CharField(max_length=100)
    ended_at = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

