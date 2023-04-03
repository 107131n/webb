from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def second(request):
    return HttpResponse("second 호출...")

def index(request):
    return render(request,
                  'secondapp/index.html')