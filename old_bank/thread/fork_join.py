import threading
import time

class BackgroundWorker(threading.Thread):
    def __init__(self, name) -> None:
        super().__init__()
        self._name = threading.current_thread().getName() + ':' + name
        
    def run(self) -> None:
        print(f'백그라운드 워커 시작 : {self._name}')
        time.sleep(3)
        print(f'백그라운드 워커 종료 : {self._name}')
        
        
print('메인 스레드 시작')

th1 = BackgroundWorker('1')
th1.start()
th2 = BackgroundWorker('2')
th2.start()

print('서브 스레드 조인')

th1.join()
th2.join()
    
print('메인 스레드 종료')