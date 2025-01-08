## 오라클 연동
import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', 1521, service_name = 'orcl') # 접속주소
conn = cx_Oracle.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')

# DB접속이 성공하면 Connection 부터 cursor() 메서드를 호출하여 객체를 가져옴
cur = conn.cursor()  # 실행결과 데이터를 담을 메모리 객체

for row in cur.execute('SELECT * FROM emp'):
    print(row)