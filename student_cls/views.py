from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from h11 import Response
from rest_framework import viewsets, response, status
from rest_framework.decorators import api_view

from student.forms import StudentForm
from student.models import Student
from student_cls.serializers import StudentsSerializer

class students_api(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


# Create your views here.
class students_details(ListView):
    queryset = Student.objects.all()
    template_name = 'students_details.html'
    context_object_name = 'students'

class student_details(DetailView):
    queryset = Student.objects.all()
    template_name = 'student_details.html'
    context_object_name = 'student'

class students_create(CreateView):
    form_class = StudentForm
    template_name = 'students_create.html'
    success_url = '/details'

class student_update(UpdateView):
    queryset = Student.objects.all()
    form_class = StudentForm
    template_name = 'student_update.html'
    success_url = '/details'

class student_delete(DeleteView):
    queryset = Student.objects.all()
    form_class = StudentForm
    template_name = 'student_delete.html'
    success_url = '/details'

@api_view(['GET'])
def get_students(request):
    student = Student.objects.all()
    serializer = StudentsSerializer(student, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def get_student(request , pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentsSerializer(student)
    return response.Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentForm(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentsSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return response.Response(status=status.HTTP_204_NO_CONTENT)



