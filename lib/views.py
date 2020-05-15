from django.shortcuts import render
from django.http import HttpResponse

def fun(request):
    return render(request,'lib/index.html')

