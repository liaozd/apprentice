#!/usr/bin/env python
# 死锁
import threading
import time

mutex_1 = threading.Lock()
mutex_2 = threading.Lock()


class MyThread1(threading.Thread):
    def run(self):
        # 1上锁
        mutex_1.acquire()

        print(self.name + ' MyThread1 up')
        time.sleep(1)

        # 对mutex_2上锁，此时堵塞，等待mutex_2释放
        mutex_2.acquire()
        print(self.name + ' MyThread1 next')
        mutex_2.release()

        # mutex_1释放
        mutex_1.release()


class MyThread2(threading.Thread):
    def run(self):
        # 2上锁
        mutex_2.acquire()

        print(self.name + 'MyThread2 up')
        time.sleep(1)

        # 对mutex_1上锁，此时堵塞，等待mutex_1释放
        mutex_1.acquire()
        print(self.name + 'MyThread2 next')
        mutex_1.release()

        # mutex_2释放
        mutex_2.release()


def main():
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
