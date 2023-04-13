from django.shortcuts import render
from django.http import HttpResponse

from .models import Member, Cart, MemCart
# Create your views here.

### oracleapp의 index 페이지
def index(request):
    return render(request,
                  "oracleapp/index.html",
                  {})
    # return HttpResponse('oracle 페이지입니다.')

##############[회원 정보]################
### 회원 정보 전체 조회하기
def getMemberList(request):
    ### 회원 정보 전체 조회하기(ORM 방식)
    # Select * From member
    # all(): 전체 조회 함수
    mem_list = Member.objects.all()
    return render(request,
                  "oracleapp/member/mem_list.html",
                  {"mem_list": mem_list})

### 회원 정보 상세 조회하기
def getMemberView(request):
    ### 변수 mem_id로 전달 받기
    # - 전달 받은 후 mem_id 출력하기
    # mem_id = request.GET["mem_id"]
    mem_id = request.GET.get("mem_id", "ERROR")

    ### 회원 정보 상세(한 건) 조회하기(ORM 방식)
    # select * from member where mem_id = mem_id

    ### 모델(M) 처리하기(한 건 조회: get() 사용)
    # - get(Member.mem_id = 전송 받은 mem_id)
    mem_view = Member.objects.get(mem_id = mem_id)
    # {"mem_id": "아이디", "mem_pass":"패스워드",
    # "mem_name": "이름", "mem_add1":"주소1" }

    # return HttpResponse()
    return render(request,
                "oracleapp/member/mem_view.html",
                {"mem_view": mem_view,
                 "mem_id": mem_id})

### 회원 정보 수정 폼 페이지
def getMemUpdateForm(request):
    # 1. 전송 데이터가 있으면 받기(get or post) GET!
    # 2. DB 입력/ 수정/ 삭제/ 조회 시 models.py 처리
    # 3. DB 결과가 있으면 html에 넘겨 주기
    mem_id = request.GET.get("mem_id", "ERROR")
    
    # {"mem_id": "아이디", "mem_pass":"패스워드",
    # "mem_name": "이름", "mem_add1":"주소1" }
    mem_view = Member.objects.get(mem_id = mem_id)

    return render(request,
                  "oracleapp/member/mem_update_form.html",
                  {"mem_id":mem_id,
                   "mem_view":mem_view})

def getMemUpdate(request):
    # 1. 전송 데이터가 있으면 받기(get or post) POST!
    # 2. DB 입력/ 수정/ 삭제/ 조회 시 models.py 처리
    # 3. DB 결과가 있으면 html에 넘겨 주기
    mem_id = request.POST.get("mem_id", "ERROR")
    mem_pass = request.POST.get("mem_pass", "ERROR")
    mem_add1 = request.POST.get("mem_add1", "ERROR")

    # msg = "아이디: {}/ 패스워드: {}/ 주소: {}".format(mem_id,
    #                                                 mem_pass,
    #                                                 mem_add1)

    ### 수정하기: model 처리
    """
        Update member
            Set mem_pass = mem_pass,
                mem_add1 = mem_add1 
        Where mem_id = mem_id
    """
    Member.objects.filter(mem_id = mem_id).update(mem_pass = mem_pass,
                                                  mem_add1 = mem_add1)
    msg = """
            <script type = 'text/javascript'>
                alert('정상적으로 수정되었습니다!');
                location.href = '/oracle/mem_view/?mem_id={}';
            </script>
    """.format(mem_id)
    return HttpResponse(msg)

def getCartList(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번 처리: 없음
    # 2번 처리: 전체 조회
    """
        Select *
        From cart;
    """
    cart_list = Cart.objects.all().order_by("-cart_no")
    """
        <cart_list의 결과값의 모양(타입)>
        [{'cart_member':'a001','cart_no':'201901010100001',
        'cart_prod':'p10100001','cart_qty':'23'},
        {'cart_member':'a001','cart_no':'201901010100001',
        'cart_prod':'p10100001','cart_qty':'23'},
        {'cart_member':'a001','cart_no':'201901010100001',
        'cart_prod':'p10100001','cart_qty':'23'}]
    """
    # 3번 처리: cart_list.html 생성
    # 4번 처리:
    return render(request,
                  "oracleapp/cart/cart_list.html",
                  {"cart_list":cart_list})

### 주문(장바구니) 상세 정보 조회 (한 건 조회)
def getCartView(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번 처리
    cart_no = request.GET.get("cart_no", "ERROR")
    cart_prod = request.GET.get("cart_prod","ERROR")

    # 2번 처리 : 2개의 PK값을 이용해서 데이터 조회 (한 건 조회)
    cart_view = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    """
        Select *
        From cart
        Where cart_no = cart_no값
        And cart_prod = cart_prod값;
    """
    # 3번 처리: cart_view.html 생성
    # 4번 처리
    return render(request,
                  "oracleapp/cart/cart_view.html",
                  {"cart_no":cart_no,
                  "cart_prod":cart_prod,
                  "cart_view":cart_view})

### 주문(장바구니) 수정 폼 페이지
def getCartUpdateForm(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번 처리
    cart_no = request.GET.get("cart_no", "ERROR")
    cart_prod = request.GET.get("cart_prod","ERROR")
    # 2번 처리
    cart_view = Cart.objects.get(cart_no=cart_no,
                                 cart_prod=cart_prod)
    # 3번 처리: cart_update_form.html 생성
    # 4번 처리
    return render(request,
                  "oracleapp/cart/cart_update_form.html",
                  {"cart_no":cart_no,
                   "cart_prod":cart_prod,
                   "cart_view":cart_view})

### 주문(장바구니) 수정 처리하기
def getCartUpdate(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번
    cart_no = request.POST.get("cart_no", "ERROR")
    cart_prod = request.POST.get("cart_prod", "ERROR")
    cart_qty = request.POST.get("cart_qty", "ERROR")

    # msg = "cart_no={}/ cart_prod={}/ cart_qty={}".format(cart_no,
    #                                                      cart_prod,
    #                                                      cart_qty)

    # 2번 처리
    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod).update(cart_qty=cart_qty)

    # 3번: html 생성 안 함
    # 4번 처리
    msg = """
        <script type = 'text/javascript'>
            alert('정상적으로 수정 완료');
            location.href = '/oracle/cart_view/?cart_no={}&cart_prod={}';
        </script>
    """.format(cart_no, cart_prod)
    return HttpResponse(msg)

### 주문(장바구니) 정보 삭제하기
def getCartDelete(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번
    cart_no = request.GET.get("cart_no", "ERROR")
    cart_prod = request.GET.get("cart_prod", "ERROR")
    
    # msg = "cart_no={}/ cart_prod={}".format(cart_no,
    #                                         cart_prod)

    # 2번 처리
    Cart.objects.filter(cart_no=cart_no,
                        cart_prod=cart_prod).delete()

    # 3번: html 생성 안 함
    # 4번 처리
    msg = """
    <script type = 'text/javascript'>
        alert('정상적으로 삭제 완료');
        location.href = '/oracle/cart_list/';
    </script>
    """
    return HttpResponse(msg)

### 주문(장바구니) 정보 등록 폼 화면 처리
def getCartInsertForm(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번: 없음
    # 2번: 없음
    # 3번: cart_insert_form.html 입력 화면 만들기
    # 4번: 
    return render(request,
                  "oracleapp/cart/cart_insert_form.html",
                  {})

### 주문(장바구니) 정보 저장 처리하기
def getCartInsert(request):
    ### 1. 전달 받을 파라메터 있으면 받기(get or post)
    ### 2. Model에서 CRUD 처리할 것이 있으면 처리(models.py)
    ### 3. Templates: html 생성
    ### 4. Model을 html 넘기기: return render()

    # 1번: O 
    cart_member = request.POST.get("cart_member","ERROR")
    cart_prod = request.POST.get("cart_prod","ERROR")
    cart_qty = request.POST.get("cart_qty","ERROR")
    cart_no = request.POST.get("cart_no","ERROR")
    
    msg = "member={} / prod={} / qty={} / no={}".format(cart_member,
                                                        cart_prod,
                                                        cart_qty,
                                                        cart_no)

    # 2번: O 
    """
        Insert into cart
            (cart_member, cart_prod, cart_qty, cart_no)
        Values
            (cart_member값, cart_prod값, cart_qty값, cart_no값)
    """
    Cart.objects.create(cart_member=cart_member,
                        cart_prod=cart_prod,
                        cart_qty=cart_qty,
                        cart_no=cart_no)
    # 3번: X 
    msg = """
        <script type = 'text/javascript'>
        alert('잘 저장되었습니다.');
        location.href = "/oracle/cart_list/";
        </script>
    """
    # 4번: X 
    return HttpResponse(msg)


#################[member join cart]#################
### 조인(join) 데이터를 사용하는 경우
# - 여러 정보를 조회할 때 주로 join 사용
# - 조회를 제외한 정보 입력/ 수정/ 삭제를 할 경우에는
#   단일 class의 테이블 정보를 사용
def getMemCartList(request):
    cart_list = MemCart.objects.all().order_by("-cart_no")
    return render(request,
                  "oracleapp/mem_cart/cart_list.html",
                  {"cart_list":cart_list})

def getMemCartView(request):

    cart_no = request.GET.get("cart_no", "ERROR")
    cart_prod = request.GET.get("cart_prod", "ERROR")

    cart_view = MemCart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    
    return render(request,
                  "oracleapp/mem_cart/cart_view.html",
                  {"cart_no":cart_no,
                  "cart_prod":cart_prod,
                  "cart_view":cart_view})

### 회원 상세 정보 보기
def getMemView(request):
    # 1번 처리: 전송 데이터 받기
    mem_id = request.GET.get("mem_id", "ERROR")
    # 2번 처리: models.py 클래스 사용
    # mem_view = Member.objects.get(mem_id=mem_id)


    # 조인이 이루어진 경우 여러건이 조회됨
    mem_view = MemCart.objects.distinct().select_related().filter(cart_member__mem_id=mem_id)
    
    # 3번 처리: html 파일 생성하기
    # 4번 처리
    return render(request,
                  "oracleapp/mem_cart/mem_view.html",
                  {"mem_view":mem_view})