from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,
                  "mainapp/index.html",
                  {})

    # return HttpResponse("GO GO ...")

### main 페이지
def main(request):
    return render(request, 
                  "mainapp/main.html",
                  {})
    # return HttpResponse('mainapp !')