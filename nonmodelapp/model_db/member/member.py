from nonmodelapp.model_db import db_sql

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

    return db_sql.setUpdate(sql)
