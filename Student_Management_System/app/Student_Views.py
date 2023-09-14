from django.shortcuts import redirect, render, HttpResponse
from .models import *

def Student_HOME(request):
    return render(request,'Student/student_home.html')