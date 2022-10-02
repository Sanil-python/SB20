from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/',views.student_data,name='student'),
    path('tea/',views.teacher_data,name='teacher'),
]
