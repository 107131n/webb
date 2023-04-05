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

#######################[HTML]##########################
def htmlView01(request):
    return render(request,
                  "frontapp/html/01_html.html",
                  {})

def linkView(request):
    return render(request,
                  "frontapp/html/02_link.html",
                  {})

def linkView2(request):
    return render(request,
                  "frontapp/html/03_link.html",
                  {})

def cssView(request):
    return render(request,
                  "frontapp/html/04_css.html",
                  {})

def tableView(request):
    return render(request,
                  "frontapp/html/05_table.html",
                  {})

def tableView2(request):
    context = {"id": "1031",
               "name": "이승협",
               "addr": "대구광역시"}
    c_list = [context, context, context] 

    return render(request,
                  "frontapp/html/06_table.html",
                  {"c_list": c_list})

def ulView(request):
    return render(request,
                  "frontapp/html/07_ul.html",
                  {})

def divView(request):
    return render(request,
                  "frontapp/html/08_div.html",
                  {})

def divView2(request):
    return render(request,
                  "frontapp/html/09_div.html",
                  {})

def iframeView(request):
    return render(request,
                  "frontapp/html/10_iframe.html",
                  {})

def cssTableView(request):
    return render(request,
                  "frontapp/html/01_table.html",
                  {})