import time
import multiprocessing
from rich import print as rprint

lock = multiprocessing.Lock()

count = 0

def one(count):
    while True:
        time.sleep(1)
        count += 1
        rprint(f"[yellow] Msg from child process [red]1 : [blue]{count}")
        if count == 5:
            lock.acquire()
            for i in range(5):
                time.sleep(1)
                count+=1
            lock.release()
        

def two(count):
    while True:
        time.sleep(1)
        count += 1
        rprint(f"[yellow] Msg from child process [red]2 : [red]{count}")       

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = one, args = (count,)).start()
    p2 = multiprocessing.Process(target = two, args = (count,)).start()