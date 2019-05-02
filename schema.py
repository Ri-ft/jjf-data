import graphene

from graphene_django.types import DjangoObjectType

from JJFDatabaseManager.masterdata.models import *

class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher

class SectionType(DjangoObjectType):
    class Meta:
        model = Section

class TestType(DjangoObjectType):
    class Meta:
        model = Test

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class GoalType(DjangoObjectType):
    class Meta:
        model = Goal

class Query(object):

    all_students = graphene.List(StudentType)
    all_teachers = graphene.List(TeacherType)

    teacher = graphene.Field(TeacherType, first_name = graphene.String(), last_name=graphene.String(), grade = graphene.Float())
    student = graphene.Field(StudentType, first_name = graphene.String(), last_name=graphene.String())
    section = graphene.Field(SectionType, name = graphene.String())
    test = graphene.Field(TestType, name = graphene.String(), grade = graphene.Float())
    project = graphene.Field(ProjectType, name = graphene.String(), grade = graphene.Float())
    quesion = graphene.Field(QuestionType, question = graphene.String(), answer = graphene.String(), score = graphene.Int())
    goal = graphene.Field(GoalType, goal = graphene.String(), completed = graphene.Boolean(), start_date = graphene.types.datetime.Date(), end_date = graphene.types.datetime.Date())
    
    

    def resolve_all_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_all_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_student(self, info, **kwargs):
        id = kwargs.get('id')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        grade = kwargs.get('grade')

        if id is not None:
            return Category.objects.get(pk=id)

        if first_name is not None:
            return Category.objects.get(first_name = first_name)

        if last_name is not None:
            return Category.objects.get(last_name = last_name)

        if grade is not None:
            return Category.objects.get(grade = grade)

        return None


    def resolve_teacher(self, info, **kwargs):

        id = kwargs.get('id')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')

        if id is not None:
            return Category.objects.get(pk=id)

        if first_name is not None:
            return Category.objects.get(first_name = first_name)

        if last_name is not None:
            return Category.objects.get(last_name = last_name)

        return None

    def resolve_section(self, info, **kwargs):

        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name = name)

        return None

    def resolve_test(self, info, **kwargs):

        id = kwargs.get('id')
        name = kwargs.get('name')
        grade = kwargs.get('grade')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name = name)

        if grade is not None:
            return Category.objects.get(grade = grade)

        return None

    def resolve_project(self, info, **kwargs):

        id = kwargs.get('id')
        name = kwargs.get('name')
        grade = kwargs.get('grade')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name = name)

        if grade is not None:
            return Category.objects.get(grade = grade)

        return None

    def resolve_question(self, info, **kwargs):

        id = kwargs.get('id')
        question = kwargs.get('question')
        answer = kwargs.get('answer')
        score = kwargs.get('score')

        if id is not None:
            return Category.objects.get(pk=id)

        if question is not None:
            return Category.objects.get(question = question)

        if answer is not None:
            return Category.objects.get(answer = answer)
        
        if score is not None:
            return Category.objects.get(score = score)

        return None

    def resolve_goal(self, info, **kwargs):

        id = kwargs.get('id')
        goal = kwargs.get('goal')
        completed = kwargs.get('completed')
        start_date = kwargs.get('start_date')
        goal_date = kwargs.get('goal_date')

        if id is not None:
            return Category.objects.get(pk=id)

        if goal is not None:
            return Category.objects.get(goal = goal)

        if completed is not None:
            return Category.objects.get(completed = completed)
        
        if start_date is not None:
            return Category.objects.get(start_date = start_date)
        
        if goal_date is not None:
            return Category.objects.get(goal_date = goal_date)

        return None

        

    

