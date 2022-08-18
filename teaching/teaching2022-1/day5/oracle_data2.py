# 커서에 접근하는 코드를 함수로 작성
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def getAllData(conn): # conn객체를 매개변수 받아서 쿼리를 실행할 함수
    cur = conn.cursor() # 커서 생성
    query = 'SELECT * FROM emp'  # emp 테이블에서 데이터 모두 가져와라
    for row in cur.execute(query): # emp 최상단에 커서가 위치하면서 모든데이터를
        print(row) # 한줄씩 출력

def getNameAndJobData(conn): 
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp' # emp 테이블 ename, job
    cur.execute(query)  # 실행
    while True:
        row = cur.fetchone()  # 한 row(레코드) 읽기
        if row is None:
            break
        else:
            print(row)

def getDeptName(conn, tup):
    cur = conn.cursor()
    # query = f"SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = '{tup[1]}'"
    #query = "SELECT * FROM dept WHERE deptno = {0} AND loc = '{1}'".format(tup[0], tup[1])
    #query = "SELECT * FROM dept WHERE deptno = :0 AND loc = :1"
    query = "SELECT * FROM dept WHERE deptno = :1 AND loc = :2"
    cur.execute(query, tup)
    row = cur.fetchone()
    print(row)

if __name__ == '__main__': # 언더바 2개씩
    print('프로그램 시작')
    # 함수호출
    scott_con = myconn() # dsn, connect() 후 접속객체 conn 리턴

    no = input('1. 부서번호를 입력하세요:')
    loc = input('2. 지역명을 입력하세요:').upper()
    tup = (no, loc)
    #print(f'부서번호: {no}, 지역: {loc}')
    getDeptName(scott_con, tup)

    print('프로그램 종료')


    # print('emp 테이블 전체 조회(SELECT *)')
    # getAllData(scott_con)
    # print('emp 2개 컬럼 조회')
    # getNameAndJobData(scott_con)