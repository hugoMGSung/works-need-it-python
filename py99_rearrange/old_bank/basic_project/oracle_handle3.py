## 오라클 연동
from sqlite3 import Cursor
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn("localhost", 1521, service_name = "orcl") # 오라클 주소
    conn = ora.connect(user="scott", password="tiger", dsn=dsn, encoding="UTF-8") # 오라클 접속
    return conn

def get_list(conn):
    cur = conn.cursor() # 실행 결과 데이터를 담을 메모리 객체
    for row in cur.execute("SELECT * FROM divtbl"):
        print(row)
        
def set_list(conn, tup):
    cur = conn.cursor()
    query = "INSERT INTO divtbl (division, names) VALUES (:1, :2)"
    cur.execute(query, tup)
    cur.close()
    conn.commit()    
        
if __name__ == '__main__':
    print('DIVISION 테이블 조회')
    get_list(myconn())
    print('DIVISION 테이블 신규 데이터 입력')
    division = input('Division 입력 :') # I002
    names = input('Names 입력 :') # 네트워크
    tup = (division, names)
    set_list(myconn(), tup)
    print('DIVISION 테이블 재조회')
    get_list(myconn())