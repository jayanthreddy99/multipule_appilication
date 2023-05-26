from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_string(request):
    return HttpResponse('<i><h1>This is app2_string </i></h1>')

def app2(request):
    return render(request,'app2.html')