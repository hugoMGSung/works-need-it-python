# 파일입출력

# 파일출력
# f = open('newfile.txt', 'w')
# f.close()

# 특정경로에 파일생성
# f = open('C:/Sources/Sample/test2.txt', 'w')
# f.close()
# print('파일이 생성되었습니다')

# newfile.txt 파일입력(읽어오기)
f = open('newfile.txt', 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line: # != line is False / == False
#         break

#     print(line)
# lines = f.readlines()
# for line in lines:
#     print(line)

# for line in f:
#     print(line)

# f.close()

# lines = f.readlines()
# print(lines)
# f.close()

for line in f:
    print(line.replace('\n', ''))

f.close()