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
        
threads = []        
print('메인 스레드 시작')
for i in range(3):
    name = f'하위스레드 {i}'
    th = BackgroundWorker(name)
    th.start()
    threads.append(th)

print('서브 스레드 조인')
for item in threads:
    item.join()
    
print('메인 스레드 종료')