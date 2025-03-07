import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import *
import pymysql

# --- 데이터베이스 연결 정보 설정 ---
# 아래 변수들은 MySQL 데이터베이스에 접속하기 위한 정보를 담고 있습니다.
host = 'localhost'  # 데이터베이스 서버 주소 (로컬 환경이므로 'localhost' 또는 '127.0.0.1' 사용)
port = 3306  # MySQL 데이터베이스 기본 포트
database = 'madang'  # 사용할 데이터베이스 이름
username = 'madang'  # 데이터베이스 접속 사용자 이름
password = 'madang'  # 데이터베이스 접속 비밀번호

# --- getValue 함수: Treeview (표)에서 선택한 항목의 정보를 가져와 Entry 위젯에 표시 ---
def getValue(event):
    """
    Treeview에서 더블 클릭으로 선택된 학생의 정보를 Entry 위젯에 채워 넣는 함수입니다.
    
    Args:
        event: Treeview에서 발생한 이벤트 객체 (더블 클릭 이벤트)
    """
    global e1, e2, e3, e4  # 전역 변수 e1, e2, e3, e4를 사용한다고 선언 (Entry 위젯)

    # Entry 위젯의 기존 내용 삭제
    e1.delete(0, END)  # e1 (학생번호) Entry 위젯의 내용을 처음(0)부터 끝(END)까지 삭제
    e2.delete(0, END)  # e2 (학생명) Entry 위젯의 내용을 처음부터 끝까지 삭제
    e3.delete(0, END)  # e3 (핸드폰) Entry 위젯의 내용을 처음부터 끝까지 삭제
    e4.delete(0, END)  # e4 (입학년도) Entry 위젯의 내용을 처음부터 끝까지 삭제

    # listBox(Treeview)에서 선택된 항목의 ID 가져오기
    row_id = listBox.selection()[0] # 선택된 항목의 ID를 가져옴. 단일선택이므로 0번째 인덱스만 가져옴
    sel_item = listBox.selection() # 선택된 항목의 ID 리스트
    
    if sel_item: # 선택된 항목이 있을 경우
        item_values = listBox.item(sel_item, 'values') # 선택된 항목의 'values'(실제 데이터) 가져오기
    
    print(item_values)  # 선택된 항목의 값을 터미널에 출력 (디버깅용)

    # Entry 위젯에 선택한 학생 정보 채워넣기
    e1.insert(0, item_values[0])  # e1 (학생번호) Entry 위젯에 선택된 학생의 학생번호를 삽입
    e2.insert(0, item_values[1])  # e2 (학생명) Entry 위젯에 선택된 학생의 학생명을 삽입
    e3.insert(0, item_values[2])  # e3 (핸드폰) Entry 위젯에 선택된 학생의 핸드폰 번호를 삽입
    e4.insert(0, item_values[3])  # e4 (입학년도) Entry 위젯에 선택된 학생의 입학년도를 삽입

# --- addValue 함수: 새로운 학생 정보 추가 ---
def addValue():
    """
    새로운 학생 정보를 데이터베이스에 추가하는 함수입니다.
    """
    global e1, e2, e3, e4  # 전역 변수 e1, e2, e3, e4를 사용한다고 선언 (Entry 위젯)

    # Entry 위젯에서 학생 정보 가져오기
    # std_id = e1.get()  # 학생번호를 가져오지만, 현재는 사용하지 않음 (자동 증가 필드)
    std_name = e2.get()  # e2 (학생명) Entry 위젯에서 학생명을 가져옴
    std_mobile = e3.get()  # e3 (핸드폰) Entry 위젯에서 핸드폰 번호를 가져옴
    std_regyear = e4.get()  # e4 (입학년도) Entry 위젯에서 입학년도를 가져옴

    # 데이터베이스 연결
    conn = pymysql.connect(host=host, user=username, passwd=password, port=port, db=database)
    cursor = conn.cursor()  # 커서 객체 생성 (데이터베이스 쿼리 실행을 위함)

    try:
        conn.begin()  # 트랜잭션 시작 (데이터 일관성 유지를 위함)

        # SQL 쿼리문 생성: students 테이블에 학생 정보 삽입
        query = 'insert into students(std_name, std_mobile, std_regyear) values(%s, %s, %s)'  
        val = (std_name, std_mobile, std_regyear)  # 삽입할 데이터 튜플
        cursor.execute(query, val)  # 쿼리 실행
        conn.commit()  # 트랜잭션 확정 (데이터베이스에 변경 사항 저장)
        lastid = cursor.lastrowid  # 마지막으로 삽입된 레코드의 ID 가져오기 (자동 증가 필드)
        print(lastid)  # 마지막으로 삽입된 레코드 ID를 터미널에 출력 (디버깅용)

        messagebox.showinfo('INSERT', '학생등록 성공!')  # 성공 메시지 박스 표시
        
        # Entry 위젯 초기화
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set() # 학생번호 입력창에 포커스 주기

    except Exception as e:  # 예외 처리 (오류 발생 시)
        print(e)  # 오류 내용 터미널에 출력
        conn.rollback()  # 트랜잭션 롤백 (변경 사항 취소)
        messagebox.showerror('INSERT', '등록정보 입력요망!')
    finally:  # 예외 발생 여부와 관계없이 항상 실행
        conn.close()  # 데이터베이스 연결 종료

    showValues()  # 데이터베이스 변경 후 Treeview 업데이트

# --- updValue 함수: 기존 학생 정보 수정 ---
def updValue():
    """
    기존 학생 정보를 수정하는 함수입니다.
    """
    global e1, e2, e3, e4  # 전역 변수 e1, e2, e3, e4를 사용한다고 선언 (Entry 위젯)
    
    # Entry 위젯에서 학생 정보 가져오기
    std_id = e1.get()  # e1 (학생번호) Entry 위젯에서 학생번호를 가져옴
    std_name = e2.get()  # e2 (학생명) Entry 위젯에서 학생명을 가져옴
    std_mobile = e3.get()  # e3 (핸드폰) Entry 위젯에서 핸드폰 번호를 가져옴
    std_regyear = e4.get()  # e4 (입학년도) Entry 위젯에서 입학년도를 가져옴

    # 데이터베이스 연결
    conn = pymysql.connect(host=host, user=username, passwd=password, port=port, db=database)
    cursor = conn.cursor()  # 커서 객체 생성 (데이터베이스 쿼리 실행을 위함)

    try:
        conn.begin() # 트랜잭션 시작

        # SQL 쿼리문 생성: students 테이블에서 해당 학생번호의 정보를 수정
        query = 'update students set std_name=%s, std_mobile=%s, std_regyear=%s where std_id=%s'
        val = (std_name, std_mobile, std_regyear, std_id)  # 수정할 데이터 튜플
        cursor.execute(query, val)  # 쿼리 실행
        conn.commit()  # 트랜잭션 확정 (데이터베이스에 변경 사항 저장)
        lastid = cursor.lastrowid  # 수정된 마지막 레코드의 ID
        print(lastid) # 수정된 마지막 레코드의 ID를 터미널에 출력 (디버깅용)

        messagebox.showinfo('UPDATE', '학생수정 성공!')  # 성공 메시지 박스 표시
        
        # Entry 위젯 초기화
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set() # 학생번호 입력창에 포커스 주기
    except Exception as e:  # 예외 처리 (오류 발생 시)
        print(e)  # 오류 내용 터미널에 출력
        conn.rollback()  # 트랜잭션 롤백 (변경 사항 취소)
    finally:  # 예외 발생 여부와 관계없이 항상 실행
        conn.close()  # 데이터베이스 연결 종료

    showValues()  # 데이터베이스 변경 후 Treeview 업데이트

# --- delValue 함수: 기존 학생 정보 삭제 ---
def delValue():
    """
    기존 학생 정보를 삭제하는 함수입니다.
    """
    global e1, e2, e3, e4  # 전역 변수 e1, e2, e3, e4를 사용한다고 선언 (Entry 위젯)

    # Entry 위젯에서 학생번호 가져오기
    std_id = e1.get()  # e1 (학생번호) Entry 위젯에서 학생번호를 가져옴

    # 데이터베이스 연결
    conn = pymysql.connect(host=host, user=username, passwd=password, port=port, db=database)
    cursor = conn.cursor()  # 커서 객체 생성 (데이터베이스 쿼리 실행을 위함)

    try:
        conn.begin()  # 트랜잭션 시작

        # SQL 쿼리문 생성: students 테이블에서 해당 학생번호의 정보 삭제
        query = 'delete from students where std_id=%s'
        val = (std_id, )  # 삭제할 학생번호 튜플
        cursor.execute(query, val)  # 쿼리 실행
        conn.commit()  # 트랜잭션 확정 (데이터베이스에 변경 사항 저장)
        lastid = cursor.lastrowid  # 삭제된 마지막 레코드의 ID
        print(lastid) # 삭제된 마지막 레코드의 ID를 터미널에 출력 (디버깅용)

        messagebox.showinfo('DELETE', '학생삭제 성공!')  # 성공 메시지 박스 표시
        
        # Entry 위젯 초기화
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set() # 학생번호 입력창에 포커스 주기
    except Exception as e:  # 예외 처리 (오류 발생 시)
        print(e)  # 오류 내용 터미널에 출력
        conn.rollback()  # 트랜잭션 롤백 (변경 사항 취소)
    finally:  # 예외 발생 여부와 관계없이 항상 실행
        conn.close()  # 데이터베이스 연결 종료

    showValues()  # 데이터베이스 변경 후 Treeview 업데이트

# --- showValues 함수: 데이터베이스에서 학생 정보 가져와 Treeview에 표시 ---
def showValues():
    """
    데이터베이스에서 모든 학생 정보를 가져와 Treeview에 표시하는 함수입니다.
    """
    # 데이터베이스 연결
    conn = pymysql.connect(host=host, user=username, passwd=password, port=port, db=database)
    cursor = conn.cursor()  # 커서 객체 생성 (데이터베이스 쿼리 실행을 위함)

    # SQL 쿼리문 생성: students 테이블에서 모든 학생 정보 선택
    query = 'select std_id, std_name, std_mobile, std_regyear from students'
    cursor.execute(query)  # 쿼리 실행
    data = cursor.fetchall()  # 쿼리 결과 (모든 학생 정보) 가져오기
    print(data)  # 데이터 터미널에 출력 (디버깅용)

    listBox.delete(*listBox.get_children())  # Treeview의 모든 기존 항목 삭제 (*: 가변인자, get_children() 은 리스트를 반환)
    # Treeview에 데이터 삽입
    for i, (std_id, std_name, std_mobile, std_regyear) in enumerate(data, start=1): # enumerate : 인덱스와 아이템을 동시에 접근
        listBox.insert("", "end", values=(std_id, std_name, std_mobile, std_regyear)) # Treeview의 마지막("end")에 항목을 추가

    cursor.close()  # 커서 객체 종료
    conn.close()  # 데이터베이스 연결 종료

# --- GUI 윈도우 설정 ---
root = Tk()  # tkinter 윈도우 생성
root.geometry("820x500")  # 윈도우 크기 설정 (가로 820, 세로 500)
root.title('학생정보 등록앱')  # 윈도우 제목 설정

root.resizable(False, False)  # 윈도우 크기 조절 불가 (가로, 세로)
myFont = Font(family='NanumGothic', size=10)  # 폰트 설정 (나눔고딕, 크기 10)

# --- 레이블(Label) 위젯 생성 및 배치 ---
tk.Label(root, text='학생번호', font=myFont).place(x=10, y=10)  # 학생번호 레이블 (x:10, y:10 위치)
tk.Label(root, text='학생명', font=myFont).place(x=10, y=40)  # 학생명 레이블 (x:10, y:40 위치)
tk.Label(root, text='핸드폰', font=myFont).place(x=10, y=70)  # 핸드폰 레이블 (x:10, y:70 위치)
tk.Label(root, text='입학년도', font=myFont).place(x=10, y=100)  # 입학년도 레이블 (x:10, y:100 위치)

# --- Entry 위젯 생성 및 배치 ---
e1 = Entry(root, font=myFont)  # 학생번호 Entry 위젯 생성
e1.config(state='readonly')
e1.place(x=140, y=10)  # 학생번호 Entry 위젯 배치 (x:140, y:10 위치)
e2 = Entry(root, font=myFont)  # 학생명 Entry 위젯 생성
e2.place(x=140, y=40)  # 학생명 Entry 위젯 배치 (x:140, y:40 위치)
e3 = Entry(root, font=myFont)  # 핸드폰 Entry 위젯 생성
e3.place(x=140, y=70)  # 핸드폰 Entry 위젯 배치 (x:140, y:70 위치)
e4 = Entry(root, font=myFont)  # 입학년도 Entry 위젯 생성
e4.place(x=140, y=100)  # 입학년도 Entry 위젯 배치 (x:140, y:100 위치)

# --- 버튼(Button) 위젯 생성 및 배치 ---
tk.Button(root, text='추가', font=myFont, command = addValue, height=3, width= 13).place(x=30, y=130)  # 추가 버튼 (x:30, y:130 위치)
tk.Button(root, text='수정', font=myFont, command = updValue, height=3, width= 13).place(x=140, y=130)  # 수정 버튼 (x:140, y:130 위치)
tk.Button(root, text='삭제', font=myFont, command = delValue, height=3, width= 13).place(x=250, y=130)  # 삭제 버튼 (x:250, y:130 위치)

# --- Treeview 위젯 생성 및 배치 ---
cols = ('학생번호', '학생명', '핸드폰', '입학년도')  # Treeview 열 이름 설정
listBox = ttk.Treeview(root, columns=cols, show='headings')  # Treeview 생성 (열 이름 사용, 제목 표시)

# Treeview 열 설정 (열 제목 설정)
for col in cols:
    listBox.heading(col, text=col) #각 열의 제목을 col 변수 값으로 설정
    listBox.grid(row=1, column=0, columnspan=2) # Treeview 위젯을 그리드 레이아웃에 배치
    listBox.place(x=10, y=200) # Treeview 위젯 배치 (x:10, y:200 위치)

showValues()  # 초기 Treeview 데이터 표시 (데이터베이스에서 학생 정보 가져와 표시)
listBox.bind('<Double-Button-1>', getValue)  # Treeview 더블 클릭 이벤트와 getValue 함수 연결

root.mainloop()  # GUI 메인 루프 시작 (GUI 윈도우 실행)
