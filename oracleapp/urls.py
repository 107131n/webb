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

    ### http://127.0.0.1:8000/oracle/mem_view/
    path('mem_view/', views.getMemberView),

    ### http://127.0.0.1:8000/oracle/mem_update_form/
    path('mem_update_form/', views.getMemUpdateForm),

    ### http://127.0.0.1:8000/oracle/mem_update/
    path('mem_update/', views.getMemUpdate),

###################[ 주문 관리 ]####################

    ### http://127.0.0.1:8000/oracle/cart_list/
    path('cart_list/', views.getCartList),

    ### http://127.0.0.1:8000/oracle/cart_view/
    path('cart_view/', views.getCartView),

    ### http://127.0.0.1:8000/oracle/cart_update_form/
    path('cart_update_form/', views.getCartUpdateForm),

    ### http://127.0.0.1:8000/oracle/cart_update/
    path('cart_update/', views.getCartUpdate),

    ### http://127.0.0.1:8000/oracle/cart_delete/
    path('cart_delete/', views.getCartDelete),

    ### http://127.0.0.1:8000/oracle/cart_insert_form/
    path('cart_insert_form/', views.getCartInsertForm),

    ### http://127.0.0.1:8000/oracle/cart_insert/
    path('cart_insert/', views.getCartInsert),

################## member와 cart join #######################
    ### http://127.0.0.1:8000/oracle/mem_cart_list/
    path('mem_cart_list/', views.getMemCartList),

    ### http://127.0.0.1:8000/oracle/mem_cart_view/
    path('mem_cart_view/', views.getMemCartView),

    ### http://127.0.0.1:8000/oracle/memview/
    path('memview/', views.getMemView),

######################상품 정보(prod)#######################

    ### http://127.0.0.1:8000/oracle/prod_list/
    path('prod_list/', views.getProdList),

    ### http://127.0.0.1:8000/oracle/prod_view/
    path('prod_view/', views.getProdView),

    ### http://127.0.0.1:8000/oracle/prod_update_form/
    path('prod_update_form/', views.getProdUpdateForm),

    ### http://127.0.0.1:8000/oracle/prod_update/
    path('prod_update/', views.getProdUpdate),

]
