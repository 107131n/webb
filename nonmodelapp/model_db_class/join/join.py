from nonmodelapp.model_db_class import db_sql

### 선택된 상품 분류에 대한 상품 정보 조회하기
# - 상품 selectbox에 넣을 값 조회
def getSelBox_Lprod_Prod(lprod_gu):
    ### SQL 구문
    sql = """
        Select prod_id, prod_name
        From lprod, prod
        Where lprod_gu = prod_lgu
            And lprod_gu = '{}'
        Order By prod_name Asc
    """.format(lprod_gu)

    return db_sql.getList(sql)


### 선택된 상품 분류 및 상품에 대한
# - 상품 상세 조회 처리

def getLprod_Prod_Buyer(lprod_gu,prod_id):
    ### SQL 구문 작성
    sql = """
        Select lprod_nm,
            prod_name, prod_sale,
            buyer_name, buyer_add1
        From lprod, prod, buyer
        Where lprod_gu = prod_lgu
            And buyer_id = prod_buyer
            And lprod_gu = '{}'
            And prod_id = '{}'
    """.format(lprod_gu, prod_id)
    return db_sql.getView(sql)


# 상품 분류 정보 전체 조회하기
def getSelBox_Lprod():
### SQL 구문 작성
    sql = """
        Select Distinct lprod_gu, lprod_nm
        From lprod, prod
        Where lprod_gu = prod_lgu
        Order By lprod_nm Asc
    """
    return db_sql.getList(sql) 