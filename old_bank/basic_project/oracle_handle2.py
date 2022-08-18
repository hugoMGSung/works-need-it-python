## 오라클 연동
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl') # 오라클 주소
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='UTF-8') # 오라클 접속
    return conn


def test01(conn):
    cur = conn.cursor() # 실행 결과 데이터를 담을 메모리 객체
    for row in cur.execute('SELECT * FROM emp'):
        print(row)

def test02(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM emp')
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row)

def test03(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM emp')
    num_rows = 10
    while True:
        rows = cur.fetchmany(num_rows)
        if not rows:
            break
        for row in rows:
            print(row)

def test04(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM emp')
    rows = cur.fetchall()   # 리턴한 객체를 한번에 리턴
    for row in rows:
        print(row)

if __name__ == '__main__':
    test01(myconn())
    print('=============================#########################################')
    test02(myconn())
    print('=============================#########################################')
    test03(myconn())
    print('=============================#########################################')
    test04(myconn())
    print('=============================#########################################')