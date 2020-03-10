import threading

def execute(num):
    return print(threading.currentThread().getName(), num)
if __name__ == '__main__':
    for i in range(1, 10):
        thread = threading.Thread(target=execute, args=(i, ))
        thread.start()