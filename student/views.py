from django.http import HttpResponse
from django.shortcuts import render
from student.forms import StudentForm
from student.models import Student


def students_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
    form = StudentForm()
    return render(request, 'students_create.html', {'form': form})

def students_details(request):
    students = Student.objects.all()
    return render(request, 'students_details.html', {'students': students})

def student_details(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student_details.html', {'student': student})

def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
    form = StudentForm(instance=student)
    return render(request, 'student_update.html', {'form': form})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return HttpResponse('success')
    form = StudentForm(instance=student)
    return render(request, 'student_delete.html', {'form': form})








