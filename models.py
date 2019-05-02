from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grade = models.DecimalField()
   

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Section(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, related_name = 'sections' on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name = 'sections')

class Test(models.Model):
    name = models.CharField(max_length=30)
    student = models.ForeignKey(Student, related_name = 'tests', on_delete=models.CASCADE)
    grade = models.DecimalField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    student = models.ForeignKey(Student, related_name = 'projects', on_delete=models.CASCADE)
    grade = models.DecimalField()

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    score = models.IntegerField()
    test = models.ForeignKey(Test, related_name = 'questions', on_delete=models.CASCADE)

class Goal(models.Model):
    goal = models.TextField()
    completed = models.BooleanField()
    start_date = models.DateField()
    goal_date = models.DateField()
    student = models.ForeignKey(Student, related_name = 'goals', on_delete=models.CASCADE)

    
