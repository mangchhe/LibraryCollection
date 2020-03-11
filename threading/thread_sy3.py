import threading
from time import sleep

count = 1

def worker_a():
    global count
    while count < 10:
        count += 1
        print(f'worker A / {count}')
        sleep(1)

def worker_b():
    global count
    while count > -10:
        count -= 1
        print(f'woker B / {count}')
        sleep(1)

if __name__ == '__main__':

    thread1 = threading.Thread(target=worker_a)
    thread2 = threading.Thread(target=worker_b)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
