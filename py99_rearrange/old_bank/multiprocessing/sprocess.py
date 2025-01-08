import multiprocessing as mp
import time

def worker():
    proc = mp.current_process()
    print(f'in worker : {proc.pid}')
    print(f'in worker : {proc.name}')
    time.sleep(3)
    print('서브프로세스 종료')
    
if __name__ == '__main__':
    proc = mp.current_process()
    print(f'in main : {proc.pid}')
    print(f'in main : {proc.name}')

    sp = mp.Process(name='서브프로세스', target=worker)
    sp.start()

    print('메인프로세스 종료')