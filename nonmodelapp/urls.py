from django.urls import path

###  from 뒤에 작성 규칙
#   - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views # .: 현재 위치

urlpatterns = [
    ### http://127.0.0.1:8000/nonmodel/
    path('', views.index),

    ### http://127.0.0.1:8000/nonmodel/index/
    path('index/', views.index),

    ###############회원 관리#################
    ### http://127.0.0.1:8000/nonmodel/mem_view/
    path('mem_view/', views.getMemberView),

    ### http://127.0.0.1:8000/nonmodel/mem_list/
    path('mem_list/', views.getMemberList),

    ### http://127.0.0.1:8000/nonmodel/mem_update_form/
    path('mem_update_form/', views.getMemUpdateForm),

    ### http://127.0.0.1:8000/nonmodel/mem_update/
    path('mem_update/', views.getMemUpdate),

    #################로그인 처리###################
    ### http://127.0.0.1:8000/nonmodel/login_form/
    path('login_form/', views.login_form),

    ### http://127.0.0.1:8000/nonmodel/login_chk/
    path('login_chk/', views.login_chk),

    ### http://127.0.0.1:8000/nonmodel/logout_chk/
    path('logout_chk/', views.logout_chk),


    # ###############주문 관리#################
    # ### http://127.0.0.1:8000/nonmodel/cart_list/
    path('cart_list/', views.getCartList),

    ### http://127.0.0.1:8000/nonmodel/cart_view/
    path('cart_view/', views.getCartView),
    
    ### http://127.0.0.1:8000/nonmodel/cart_update_form/
    path('cart_update_form/', views.getCartUpdateForm),

    ### http://127.0.0.1:8000/nonmodel/cart_update/
    path('cart_update/', views.getCartUpdate),
    
    ### http://127.0.0.1:8000/nonmodel/cart_insert_form/
    path('cart_insert_form/', views.getCartInsertForm),
    
    ### http://127.0.0.1:8000/nonmodel/cart_insert/
    path('cart_insert/', views.getCartInsert),
    
    ### http://127.0.0.1:8000/nonmodel/cart_delete/
    path('cart_delete/', views.getCartDelete),


    #############검색으로 상품 상세 조회 처리########### 
    ### http://127.0.0.1:8000/nonmodel/search_prod/
    path('search_prod/', views.getSearchProd),

    ################# [메일 발송 처리] ##################
    ### http://127.0.0.1:8000/nonmodel/email_form/
    path('email_form/', views.getEmailForm),

    ### http://127.0.0.1:8000/nonmodel/email_send/
    path('email_send/', views.emailSend),

]