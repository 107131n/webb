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

