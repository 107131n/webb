import cx_Oracle

# DB 접속 기능 함수 정의
def getDBConn_Cursor():
    dsn = cx_Oracle.makedsn("localhost",1521 ,"xe")
    conn = cx_Oracle.connect("gwangju_a","dbdb",dsn)
    cursor = conn.cursor()
    
    return conn, cursor

# - 조회 결과에서 컬럼명 추출하기 기능 정의
def getColName(cursor):
    col = []
    for t in cursor.description:
        col.append(t[0].lower())
    return col

# - "한 건 조회" 시 딕셔너리로 변환하는 기능 정의
def getFetchOne(cursor, row):
    # 컬럼명 조회 함수 호출
    col = getColName(cursor)
    
    dict_row = {}
    for i in range(0,len(col), 1):
        dict_row[col[i]] = row[i]
    
    return dict_row

# - "여러 건 조회" 시 딕셔너리로 변환하는 기능 정의
def getFetchAll(cursor, rows):
    
    # 컬럼명 조회 함수 호출
    col = getColName(cursor)
    
    list_row = []
    for t in rows:
        dict_temp = {}
        for i in range(0, len(col),1):
            # print(col[i], t[i])
            dict_temp[col[i]] = t[i]
        list_row.append(dict_temp)
        
    return list_row

# - 커서 및 connect 접속 해제하는 기능 정의
def DBClose(cursor, conn):
    cursor.close()
    conn.close()