from time import sleep, time

start_time = time()

def count(name):
    for i in range(200000):
        print(name,' : ', i)

name_list = ['p1','p2','p3','p4']

for name in name_list:
    count(name)

print('--- %s seconds ---' % (time() - start_time))