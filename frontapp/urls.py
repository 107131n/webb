
from django.urls import path

###  from 뒤에 작성 규칙
#   - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views # .: 현재 위치

urlpatterns = [
    ### http://127.0.0.1:8000/front/
    path('', views.index),

    ### http://127.0.0.1:8000/front/image/
    path('image/', views.imageView), 

    ### http://127.0.0.1.8000/front/css_1/
    path('css_1/', views.cssView1),

    ### http://127.0.0.1.8000/front/css_2/
    path('css_2/', views.cssView2),

    ### http://127.0.0.1.8000/front/css_3/
    path('css_3/', views.cssView3),

    ### http://127.0.0.1.8000/front/javascript1/
    path('javascript1/', views.javascriptView1),

    ### http://127.0.0.1.8000/front/javascript2/
    path('javascript2/', views.javascriptView2),
    
    ### http://127.0.0.1.8000/front/javascript3/
    path('javascript3/', views.javascriptView3),
    
    ### http://127.0.0.1.8000/front/01_html/
    path('01_html/', views.htmlView01),

    ### http://127.0.0.1.8000/front/02_link/
    path('02_link/', views.linkView),

    ### http://127.0.0.1.8000/front/03_link/
    path('03_link/', views.linkView2),

    ### http://127.0.0.1.8000/front/04_css/
    path('04_css/', views.cssView),

    ### http://127.0.0.1.8000/front/05_table/
    path('05_table/', views.tableView),

    ### http://127.0.0.1.8000/front/06_table/
    path('06_table/', views.tableView2),

    ### http://127.0.0.1.8000/front/07_ul/
    path('07_ul/', views.ulView),

    ### http://127.0.0.1.8000/front/08_div/
    path('08_div/', views.divView),

    ### http://127.0.0.1.8000/front/09_div/
    path('09_div/', views.divView2),

    ### http://127.0.0.1.8000/front/10_iframe/
    path('10_iframe/', views.iframeView),

    ### http://127.0.0.1.8000/front/01_cssTable/
    path('01_cssTable/', views.cssTableView),


]
