from multiprocessing import Pool

def work(x):
    print(x)
    
if __name__ == '__main__':
    pool = Pool(4) # core 4개 사용
    data = range(1, 100) # 1~99까지 반복 범위
    pool.map(work, data)
    