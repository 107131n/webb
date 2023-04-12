from django.db import models

### 데이터타입 라이브러리 정의
# - DB에서 varchar2 또는 char 등 문자열 타입
from django.db.models.fields import CharField
# - DB에서 number 또는 integer 등 숫자형 타입
from django.db.models.fields import IntegerField

# Create your models here.

### models.py에 클래스가 추가되는 경우 무조건 아래 명령 실행
# >python manage.py makemigrations oracleapp 
# >python manage.py migrate

### 실제 DB에 있는 테이블의 형상과 동일하게 생성하기
# - 테이블명, 컬럼명은 실제 이름과 동일하게 작성해야 함
# - 테이블은 class로 생성, 컬럼명은 변수로 정의

### 회원 정보 테이블
class Member(models.Model):
    mem_id = CharField(primary_key=True,
                       max_length= 5, null=False)
    mem_pass = CharField(max_length=15, null=False)
    mem_name = CharField(max_length=20, null=False)
    mem_add1 = CharField(max_length=100, null=False)

    ### 해당 클래스가 사용할 실제 테이블 및 앱 지정
    class Meta:
        ### 실제 사용할 테이블 이름 정의
        db_table = "member"

        ### 사용할 앱 이름 정의
        app_label = "oracleapp"

        ### 외부 데이터베이스에 테이블 존재 여부 확인
        # 존재하면 False
        # 존재하지 않으면 True
        # => 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed = False

### 주문 정보(장바구니) cart 테이블 클래스 생성하기
class Cart(models.Model):
    cart_member = CharField(max_length=15, null=False)
    ### cart_no만 PK로 지정
    cart_no = CharField(primary_key=True, max_length=13, null=False)
    cart_prod = CharField(max_length=10, null=False)
    cart_qty = IntegerField(max_length=8, null=False)

    class Meta:
        ### 실제 사용할 테이블 이름 정의
        db_table = "cart"

        ### 사용할 앱 이름 정의
        app_label = "oracleapp"

        ### 외부 데이터베이스에 테이블 존재 여부 확인
        # 존재하면 False
        # 존재하지 않으면 True
        # => 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed = False