from django.http import HttpResponseRedirect #create at the time of view_student 
from django.shortcuts import render
from django.urls import reverse  #create at the time of view_student 
from .models import Student

# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

#create view_student   

def view_student(request, id):
  student = Student.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))