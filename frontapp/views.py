from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,
                  "frontapp/index.html",
                  {})

### 이미지 보여주기
def imageView(request):
    return render(request,
                  "frontapp/01_image.html",
                  {})
    # return HttpResponse("이미지 테스트")


def cssView1(request):
    return render(request,
                  "frontapp/02_css1.html",
                  {})

def cssView2(request):
    return render(request,
                  "frontapp/02_css2.html",
                  {})

def cssView3(request):
    return render(request,
                  "frontapp/02_css3.html",
                  {})

def javascriptView1(request):
    return render(request,
                  "frontapp/01_javascript1.html",
                  {})

def javascriptView2(request):
    return render(request,
                  "frontapp/01_javascript2.html",
                  {})

def javascriptView3(request):
    return render(request,
                  "frontapp/01_javascript3.html",
                  {})