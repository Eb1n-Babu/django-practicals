from django.urls import path
from student_cls.views import students_details,students_create , student_update , student_delete ,student_details ,students_api
from student_cls.views import get_student ,get_students ,create_student ,update_student ,delete_student
urlpatterns = [
    path('',students_create.as_view(),name='students_create'),
    path('details/',students_details.as_view(),name='students_details'),
    path('details/<int:pk>/',student_details.as_view(),name='student_details'),
    path('details/<int:pk>/update/',student_update.as_view(),name='student_update'),
    path('details/<int:pk>/delete/',student_delete.as_view(),name='student_delete'),

    path('details/api/',students_api.as_view({'get': 'list', 'post': 'create'})),
    path('details/api/<int:pk>/',students_api.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('details/get_students/',get_students),
    path('details/create_student/',create_student),
    path('details/get_student/<int:pk>/',get_student),
    path('details/get_student/<int:pk>/update_student/',update_student),
    path('details/get_student/<int:pk>/delete_student/',delete_student),


]
