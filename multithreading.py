import multiprocessing
import threading
import time

st=time.time()

def india():
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')
def canada():
    for i in range(1,11):
        time.sleep(0.5)
        print(f'canada : {i}')
def usa():
    for j in range(1,11):
        time.sleep(0.5)
        print(f'usa : {j}')
def uk():
    for j in range(1,11):
        time.sleep(0.5)
        print(f'uk : {j}')

def common():
    t1=threading.Thread(target=india,args=())
    t2=threading.Thread(target=canada,args=())
    t1.start()
    t2.start()
def common2():
    t3=threading.Thread(target=usa,args=())
    t4=threading.Thread(target=uk,args=())
    t3.start()
    t4.start()

if __name__=="__main__":
    cpu1=multiprocessing.Process(target=common,args=())
    cpu2=multiprocessing.Process(target=common2,args=())
    cpu1.start()
    cpu2.start()
    cpu1.join()
    cpu2.join()
    print(f'MAIN PROCESSOR EXIT')
    print(f'Total time : {time.time()-st}')
