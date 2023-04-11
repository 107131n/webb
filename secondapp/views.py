from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Member
# from .model import Member
def second(request):
    return HttpResponse("second 호출...")

def index(request):
    return render(request,
                  'secondapp/index.html')

def cssTestView(request):
    return render(request,
                  'secondapp/css_test.html')

def getMemberAll(request):
    mem_all = Member.objects.all()
    return render(request,
                  'secondapp/member/mem_all.html',
                  {"mem_all": mem_all})