from django.urls import path
from . import views

urlpatterns = [
    path('student_info/',views.basic_demo,name='basic_demo'),
    path("add_student/",views.add,name='add_student'),
    path("form/",views.form,name='form'),
    path('update/',views.update,name='update_student'),
    path('search_student/',views.search,name='search_student'),
    path('view_students/',views.view,name='view_students'),
    path('delete_student/<int:roll_no>/',views.delete,name='delete_student'),
    
]