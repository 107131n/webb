from django.urls import path
from . import views


urlpatterns = [
    ### http://127.0.0.1.8000/third/
    path('', views.index),

    ### http://127.0.0.1.8000/third/index/
    path('index/', views.index),
    
]