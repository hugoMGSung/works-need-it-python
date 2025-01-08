# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수 
memory = [] #lists()
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

# 노드추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData: # 첫노드 앞
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head # 제일 앞으로
    while current.link != None: # 중간노드 
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # current.link == None 까지 온것
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드삭제
def deleteNode(deleteData):
    global memory, pre, current, head

    if head.data == deleteData: # 첫번째 노드 삭제
        current = head
        head = head.link # 두번째 노드로 변경
        del(current)
        return

    current = head
    while current.link != None:  # 첫번째 이외 노드 삭제
        pre = current # 모두 첫번째 노드 가리킴
        current = current.link # 두번째 노드를 가리킴
        if current.data == deleteData:
            pre.link = current.link  # current가리키는 노드를 pre가 가리키도록(삭제)
            del(current) 
            return

# 노드검색
def findNode(findData):
    global memory, pre, current, head

    current = head # 첫번째노드부터
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link # 다음노드
        if current.data == findData:
            return current

    return Node() # 빈노드 반환   

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0] # 다현
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두번째 노드 이후 4번 반복
        pre = node
        node = Node()
        node.data = data # 정연, 쯔위, 사나, 지효 순
        pre.link = node
        memory.append(node)

    printNodes(head) # 전체출력    

    print('노드 추가 ---- ')

    insertNode('재남', '문별') # 맨마지막 노드 추가
    printNodes(head)

    insertNode('사나', '솔라') # 중간 노드추가
    printNodes(head)

    insertNode('다현', '화사') # 맨앞에 화사노드 추가
    printNodes(head) 

    print('노드 삭제 ----')

    deleteNode('화사')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('재남') # 데이터 삭제X
    printNodes(head)

    print('노드 검색 ----')

    result = findNode('정연')
    if result.data != None:
        print('데이터 찾았습니다')
    else:
        print('검색한 데이터 없습니다')

    result = findNode('재남')
    if result.data != None:
        print('데이터 찾았습니다')
    else:
        print('검색한 데이터 없습니다')
