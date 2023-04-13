from django.urls import path
###  from 뒤에 작성 규칙
#   - 폴더 경로 또는 폴더 경로 + 파일명

from . import views

urlpatterns = [

    ### http://127.0.0.1.8000/second/
    path('', views.index),

    ### http://127.0.0.1.8000/second/index/
    path('index/', views.index),

    ### http://127.0.0.1.8000/second/cart_list/
    path('cart_list/', views.getCartList),

]
