import threading
import time
def sleeper(n,name):
    print('hi I {}'.format(name))
    time.sleep(n)
    print('dddd')
liss=[]
t = threading.Thread(target=sleeper,name='Thread1',args=(2,'thread1'))
for i in range(5):
    t = threading.Thread(target=sleeper,name='Thread{}'.format(i),args=(2,'thread{}'.format(i)))
    t.start()
    liss.append(t)
for t in liss:
    t.join()
