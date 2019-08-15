#!/usr/bin/env python
import threading
import time

global_var = 0


def test1():
    global global_var
    for i in range(100):
        global_var += 1
    print(f'In test1 global_var={global_var}')


def test2():
    print(f'In test2 global_var={global_var}')


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print(f'In main() global_var={global_var}')


if __name__ == '__main__':
    main()
