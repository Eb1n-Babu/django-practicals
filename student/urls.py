from django.urls import path
from .views import students_create , students_details , student_details , student_update , student_delete

urlpatterns = [
    path('',students_create,name='students_create'),
    path('details/',students_details,name='students_details'),
    path('details/<int:id>/',student_details,name='student_details'),
    path('details/<int:id>/update',student_update,name='student_update'),
    path('details/<int:id>/delete',student_delete,name='student_delete'),

]
