from multiprocessing import Process
import threading
import time

def f(name):
    time.sleep(3)
    print ("hello", name)

if __name__ == '__main__':
    time_start = time.time();
    p1 = Process(target=f, args=("xiodi",))
    p2 = Process(target=f, args=("dadi",))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    time_end = time.time()
    print time_end - time_start