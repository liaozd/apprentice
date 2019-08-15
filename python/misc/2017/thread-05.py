#!/usr/bin/env python
# 共享全局变量
import threading


def test1(temp):
    temp.append(33)
    print(f'In test1 temp {temp}')


def test2(temp):
    print(f'In test2 temp {temp}')


g_nums = [1, 2]


def main():
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    t2.start()
    print(f'In main thread g_num = {g_nums}')


if __name__ == '__main__':
    main()
