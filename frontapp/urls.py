
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

    ###http://127.0.0.1.8000/front/css_1/
    path('css_1/', views.cssView1),

    ###http://127.0.0.1.8000/front/css_2/
    path('css_2/', views.cssView2),

    ###http://127.0.0.1.8000/front/css_3/
    path('css_3/', views.cssView3),

    ###http://127.0.0.1.8000/front/javascript1/
    path('javascript1/', views.javascriptView1),

    ###http://127.0.0.1.8000/front/javascript2/
    path('javascript2/', views.javascriptView2),
    
    ###http://127.0.0.1.8000/front/javascript3/
    path('javascript3/', views.javascriptView3),


]
