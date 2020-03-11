from time import sleep, time
import multiprocessing

start_time = time()

def count(name):
    for i in range(200000):
        print(name, ' : ', i)

name_list = ['p1','p2','p3','p4']

if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=2)
    pool.map(count, name_list)
    pool.close()
    pool.join()

    print('--- %s seconds ---' % (time() - start_time))