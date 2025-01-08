import multiprocessing as mp

# proc = mp.current_process()
# print(f'{proc.pid}, {proc.name}')

def worker():
    print("서브프로세스 종료")


if __name__ == "__main__":
    p = mp.Process(name="서브프로세스", target=worker)
    p.start()