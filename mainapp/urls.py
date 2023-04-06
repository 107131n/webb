from django.urls import path

###  from 뒤에 작성 규칙
#   - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views # .: 현재 위치

urlpatterns = [
    ### http://127.0.0.1:8000/main/main/
    path('main/', views.main )
]

