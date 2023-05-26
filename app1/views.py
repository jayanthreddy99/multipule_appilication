from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app1_string(request):
    return HttpResponse('<i><h1>This is app1_string </i></h1>')

def app1(request):
    return render(request,'app1.html')