from django.shortcuts import render
from django.http import HttpResponse

from .models import Member
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