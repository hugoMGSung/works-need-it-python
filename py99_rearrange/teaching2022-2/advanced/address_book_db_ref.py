# 주소록 프로그램 v2.0
# 작성일 : 2022-05-05
# 작성자 : HugoMG Sung
# 설  명 : 어린이날도 못논다. ㅜㅜ;
import os
import cx_Oracle as ora

# 연락처 클래스
class Contact:
    name = ''; phone_num = ''; e_mail = ''; addr = ''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:
        str_val = (f'이  름 : {self.name}\n'
                   f'핸드폰 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'==============================')
        return str_val

def initDB():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def run():
    # lst_contact = [] # 빈 리스트 생성
    conn = initDB()
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            set_contact(conn)
            # lst_contact.append(contact)
            input()  # 아무값도 엔터 대기
            clearConsole()
        elif sel_menu == 2: #연락처 출력
            clearConsole()
            get_contact(conn)
            input() # 엔터 대기
            clearConsole()
        elif sel_menu == 3:
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(conn, name)
            input()
            clearConsole()
        elif sel_menu == 4:
            break
        else:
            clearConsole()

# 주소록 입력함수
def set_contact(conn):
    name, phone_num, e_mail, addr = \
        input('정보입력(이름,핸드폰,이메일,주소(구분자 /)) >').split('/')
    contact = Contact(name, phone_num, e_mail, addr)
    
    cur = conn.cursor()
    query = 'INSERT INTO contacts VALUES (SEQ_CONTACTS.nextval, :1, :2, :3, :4)'    
    # db처리
    tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
    cur.execute(query, tup)
    conn.commit()
    cur.close()
    print('주소록 추가')

# 주소록 전체 출력
def get_contact(conn):
    cur = conn.cursor()
    
    for row in cur.execute('SELECT name, phone_num, e_mail, addr FROM contacts ORDER BY idx'):
        contact = Contact(row[0], row[1], row[2], row[3])
        print(contact)
        
    print('주소록 조회 완료')
    

# 주소록 삭제
def del_contact(conn, name):
    cur = conn.cursor()
    query = "delete from contacts where NAME = '{name}'"
    cur.execute(query)
    conn.commit()
    cur.close()
    
    print('주소록 삭제')
    
    

def get_menu():
    str_menu = ('--주소록 프로그램 v1.1--\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    menu = input('메뉴입력 : ')
    return int(menu)

def clearConsole():
    command = 'clear' # mac, unix, linux 화면클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' # windows, dos 화면클리어 명령어
    os.system(command)


if __name__ == '__main__':
    run()