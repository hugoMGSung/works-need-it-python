'''
MySQL 처리
1. 필요라이브러리 설치 아래 진행 오류나면 다른 라이브러리도 설치
apt-get install python3-mysqldb
apt-get install python3-dev
apt-get install libmysqlclient-dev
pip3 install MySQL-python3
'''
import MySQLdb

db = MySQLdb.connect(host='210.119.12.52', \
                    user='test_usr', \
                    passwd='mysql_p@ssw0rd', \
                    db='shopdb', \
                    charset='utf8')
cur = db.cursor()
cur.execute('select * from producttbl')

while True:
    product = cur.fetchone()
    if not product: 
        break

    print(product)

cur.close()
db.close()