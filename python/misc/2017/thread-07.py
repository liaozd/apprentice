#!/usr/bin/env python
# 互斥锁

import threading
import time

mutex = threading.Lock()  # Mutual exclusion

g_num = 100


def test1():
    global g_num
    for i in range(1000000):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁
    print(f'In test1 {g_num}')


def test2():
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print(f'In test2 {g_num}')


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()
    time.sleep(1)
    print(f'In main {g_num}')


if __name__ == '__main__':
    main()
