# oracle_data
# cx_oracle 설치 : pip install cx_oracle
import cx_Oracle as ora

#makedsn('호스트명/ip주소', portnum, '서비스명')
dsn = ora.makedsn('localhost', 1521, service_name='orcl')
#connect(user, password, dsn, encoding)
conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')

cur = conn.cursor()

try:
    for row in cur.execute('SELECT * FROM emp'):
        print(row)
    # cur.execute('SELECT COUNT(*) FROM emp')
    # result = cur.fetchone()
    # print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 13번라인 확인요 : {e}')
finally:
    cur.close()  # 커서 닫고
    conn.close() # 접속 닫음