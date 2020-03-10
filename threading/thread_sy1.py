# 코드가 동기화 구현이 안되어서 좋지 않은 예

import threading

total = 0

def add_total(amount):
    global total
    total += amount
    print(threading.currentThread().getName() + ' Not Synchronized : ', total)

if __name__ == '__main__':
    for i in range(10000):
        thread = threading.Thread(target=add_total, args=(1,))
        thread.start()