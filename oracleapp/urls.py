from django.urls import path

###  from 뒤에 작성 규칙
#   - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views # .: 현재 위치

urlpatterns = [
    ### http://127.0.0.1:8000/oracle/
    path('', views.index),

    ### http://127.0.0.1:8000/oracle/index/
    path('index/', views.index),

###################[ 회원 관리 ]####################
    ### http://127.0.0.1:8000/oracle/mem_list/
    path('mem_list/', views.getMemberList),
]
