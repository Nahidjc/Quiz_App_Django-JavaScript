from django.shortcuts import render
from .models import Exam
# Create your views here.


def index(request):
    exams = Exam.objects.all()
    return render(request, 'index.html', context={'exams': exams})
