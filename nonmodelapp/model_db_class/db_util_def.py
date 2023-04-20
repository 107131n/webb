### 오라클 라이브러리 불러들이기
import cx_Oracle

### 클래스 내부의 모든 함수에는 매개 변수 self 키워드를 넣어야 함(규칙)
# - self: self가 표시된 변수들은 전역 변수 또는 외부 파일에서 직접 접근 가능
# - class 내부 함수 간의 호출을 위해서 self를 붙여야 함
class DB_Util:

    ### 생성자 정의하기
    def __init__(self):
        ### 클래스 생성과 동시에 DB 연결 및 커서 받아 오는 기능 수행
        self.getDBConn_Cursor()

    # DB 접속 기능 함수 정의
    def getDBConn_Cursor(self):
        dsn = cx_Oracle.makedsn("localhost",1521 ,"xe")
        self.conn = cx_Oracle.connect("gwangju_a","dbdb",dsn)
        self.cursor = self.conn.cursor()

    # - 조회 결과에서 컬럼명 추출하기 기능 정의
    def getColName(self):
        col = []
        for t in self.cursor.description:
            col.append(t[0].lower())
        return col

    # - "한 건 조회" 시 딕셔너리로 변환하는 기능 정의
    def getFetchOne(self, sql):
        try:
            ### 구문 실행하기
            self.cursor.execute(sql)

            ### 결과 추출하기
            row = self.cursor.fetchone()

            ### 조회 결과가 없을 떄 처리하기
            if row == None:
                self.DBClose()
                return {"Result" : "Data_None"} 

            # 컬럼명 조회 함수 호출
            col = self.getColName()
            
            dict_row = {}
            for i in range(0,len(col), 1):
                dict_row[col[i]] = row[i]

            self.DBClose()
            
        except:
            self.DBClose()
            return {"Result" : "DB_ERROR"} 
        
        return dict_row

    # - "여러 건 조회" 시 딕셔너리로 변환하는 기능 정의
    def getFetchAll(self, sql):
        try:
            ### 구문 실행하기
            self.cursor.execute(sql)

            ### 결과 추출하기
            rows = self.cursor.fetchall()

            ### 조회 결과가 없을 떄 처리하기
            if rows == None:
                self.DBClose()
                return [{"Result" : "Data_None"}] 

            # 컬럼명 조회 함수 호출
            col = self.getColName()
            
            list_row = []
            for t in rows:
                dict_temp = {}
                for i in range(0, len(col),1):
                    # print(col[i], t[i])
                    dict_temp[col[i]] = t[i]
                list_row.append(dict_temp)
            
            self.DBClose()

        except:
            self.DBClose()
            return [{"Result" : "Data_None"}]
        
        return list_row

    ##### - 데이터 입력(C), 수정(U), 삭제(D) 처리 기능 정의
    def setCUD(self,sql):
        ### 구문 실행하기
        self.cursor.execute(sql)

        ### 데이터 수정/ 삭제/ 입력 시 아래 적용해야 함
        self.conn.commit()

        ### DB 접속 해제하기
        self.DBClose()


    # - 커서 및 connect 접속 해제하는 기능 정의
    def DBClose(self):
        ### 커서 반환
        self.cursor.close()
        
        ### 접속 해제
        self.conn.close()
