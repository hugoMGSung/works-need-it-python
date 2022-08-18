import pyzbar.pyzbar as pyzbar
import cv2
import time
from datetime import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pymysql

my_db = pymysql.connect(
    user='root',
    passwd='mysql_p@ssw0rd',
    host='127.0.0.1',
    db='access_detection',
    charset='utf8'
)

def get_accurmember(code):
    # code 사용
    cursor = my_db.cursor(pymysql.cursors.DictCursor)
    temp = code.strip().split('|')
    if (len(temp) < 2): return False
    
    sql = 'SELECT * FROM member_info'
    cursor.execute(sql)
    dbresult = cursor.fetchall()

    result = next((item for item in dbresult if (item['phone_num'] == temp[0] and item['name'] == temp[1])), False)

    if result == False: return False
    else: 
        return True

def set_accesslog(code):
    # code 사용
    cursor = my_db.cursor(pymysql.cursors.DictCursor)
    temp = code.strip().split('|')
    if (len(temp) < 2): return False

    sql = '''INSERT INTO `access_detection`.`access_log` 
                (`access_dt`, `phone_num`, `name`, `access_available`) 
             VALUES 
                ('{0}', '{1}', '{2}', '1');'''.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), temp[0], temp[1])
    cursor.execute(sql)
    my_db.commit()


cap = cv2.VideoCapture(0)
# PKNU2020Fighting!!
hashVal = 'D67C69FFACCF947DBEAD024F8FF722D0'
font = ImageFont.truetype('./fonts/NANUMGOTHIC.ttf', 20) # 글꼴파일을 불러옴

i = 0
while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = pyzbar.decode(gray)
    qrcode_data = ''

    for d in decoded:
        x, y, w, h = d.rect

        qrcode_data = d.data.decode("utf-8")
        qr_type = d.type

        if (qr_type == 'QRCODE'): # QR코드라면 
            ## 이미지 저장
            capname = datetime.now().strftime('%Y%m%d%H%M%S')
            cv2.imwrite('./qrcapture/{0}_cap.png'.format(capname), gray)

            # img 변경
            simg = cv2.imread('./qrcapture/{0}_cap.png'.format(capname))
            img_pil = Image.fromarray(simg)
            draw = ImageDraw.Draw(img_pil)

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            text = '%s (%s)' % (str(qrcode_data).encode('utf-8').decode('utf-8'), qr_type)
            draw.text((0, 0),  text, font=font, fill=(255,255,255,0))
        
            simg = np.array(img_pil)
            cv2.rectangle(simg, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # print("{}".format(qrcode_data))
            # cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
            #             1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('capimg', simg)
            print(qrcode_data)
            ## 여기서 처리
            ## DB처리
            result = get_accurmember(qrcode_data)
            
            if result == True:
                set_accesslog(qrcode_data)
                print('출입허가~!!')
            else:
                print('출입불가!!!!')

            time.sleep(3)

    cv2.imshow('img', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        i += 1
        # print("{}".format(qrcode_data))
        cv2.imwrite('D:\\c_%03d.jpg' % i, img)

cap.release()
cv2.destroyAllWindows()