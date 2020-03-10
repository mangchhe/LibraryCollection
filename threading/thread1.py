'''
https://hamait.tistory.com/833
'''

import threading
from time import sleep

def Thread(name, sec):
    print('--- do something ---')
    sleep(sec)

if __name__ == '__main__':

    t = threading.Thread(target=Thread, args=('Thread-1', 3))

    t.start()
    t.join() # 해당 스레드가 종료될 때까지 대기한다.

    print('--- exit ---')