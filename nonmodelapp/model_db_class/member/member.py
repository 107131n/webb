from nonmodelapp.model_db_class import db_sql
from django.http import HttpResponse
# 회원 전체 조회하기
def getMemberList():

    ### 구문 작성
    sql = """
        Select mem_id, mem_pass, mem_name, mem_add1
        From member
    """
    return db_sql.getList(sql)

# 회원 한 건 조회하기
def getMember(mem_id):

    ### 구문 작성
    sql ="""
            Select mem_id, mem_pass, mem_name, mem_add1
            From member
            Where mem_id = '{}'
        """.format(mem_id)

    return db_sql.getView(sql)

### 수정 처리하기
def setMemberUpdate(mem_pass, mem_add1, mem_id):

    ### 구문 작성
    sql = """
        Update member
            Set mem_pass = '{}',
                mem_add1 = '{}'
        Where mem_id = '{}'
    """.format(mem_pass, mem_add1, mem_id)

    return db_sql.setCUD(sql)

### 회원 로그인 인증 처리(아이디, 패스워드)
def getLoginChk(mem_id, mem_pass):
    
    ### 구문 작성    
    sql = """
        Select mem_id, mem_pass, mem_name, mem_add1
        From member
        Where mem_id = '{}'
        And mem_pass = '{}'
    """.format(mem_id, mem_pass)

    return db_sql.getView(sql)

    