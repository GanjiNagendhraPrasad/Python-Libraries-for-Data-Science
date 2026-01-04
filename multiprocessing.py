import multiprocessing
import time
import os

st = time.time()

def india():
    print(f'cpu1 ID : {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')

def usa():
    print(f'cpu2 ID : {os.getpid()}')
    for j in range(1,11):
        time.sleep(0.5)
        print(f'usa : {j}')

if __name__=="__main__":
    print(f'MAIN PROCESSOTID : {os.getpid()}')
    cpu1=multiprocessing.Process(target=india,args=())
    cpu2=multiprocessing.Process(target=usa,args=())

    cpu1.start()
    cpu2.start()

    cpu1.join()
    cpu2.join()

    print(f'MAIN PROCESSOR EXIST')
    print(f'total time = {time.time() - st}')