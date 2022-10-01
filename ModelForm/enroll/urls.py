from django.urls import path
from . import views

urlpatterns = [
    path('registration/<int:pk>',views.studentregistrationform,name='details'),
]