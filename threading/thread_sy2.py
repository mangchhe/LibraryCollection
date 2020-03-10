# 코드가 동기화 구현이 안되어서 좋은 예

import threading

total = 0
lock = threading.Lock()

def add_total(amount):
    global total
    lock.acquire()
    try:
        total += amount
    finally:
        lock.release()
    print(threading.currentThread().getName()+ ' Synchronisze :',total)

    '''
    global total
    with lock:
        total += amount
    print (threading.currentThread().getName()+' Synchronized  :',tot)
    '''

if __name__ == '__main__':
    for i in range(10000):
        thread = threading.Thread(target=add_total, args=(1, ))
        thread.start()