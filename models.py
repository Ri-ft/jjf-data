from django.db import models

#necessary models
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grade = models.DecimalField()
   

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Section(models.Model):
    name = models.CharField(max_length=30)
    #each section is taught by a teacher
    teacher = models.ForeignKey(Teacher, related_name = 'sections' on_delete=models.CASCADE)
    #student can potentially be in many sections, and a section has many students
    students = models.ManyToManyField(Student, related_name = 'sections')

class Test(models.Model):
    name = models.CharField(max_length=30)
    #each test pertains to a student
    student = models.ForeignKey(Student, related_name = 'tests', on_delete=models.CASCADE)
    grade = models.DecimalField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    #each project pertains to a student
    student = models.ForeignKey(Student, related_name = 'projects', on_delete=models.CASCADE)
    grade = models.DecimalField()

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    score = models.IntegerField()
    #each question pertains to a test
    test = models.ForeignKey(Test, related_name = 'questions', on_delete=models.CASCADE)

class Goal(models.Model):
    goal = models.TextField()
    completed = models.BooleanField()
    start_date = models.DateField()
    goal_date = models.DateField()
    #each goal pertains to a student
    student = models.ForeignKey(Student, related_name = 'goals', on_delete=models.CASCADE)

    
