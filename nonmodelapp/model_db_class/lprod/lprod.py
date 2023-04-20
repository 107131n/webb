
from nonmodelapp.model_db_class import db_sql

### 상품 분류 정보 전체 조회하기
def getLprodList():
    ### SQL 구문
    sql = """
        Select lprod_gu, lprod_nm
        From lprod
        Order By lprod_nm ASC
    """

    return db_sql.getList(sql)