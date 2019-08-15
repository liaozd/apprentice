import time
import threading


def sing():
    for i in range(5):
        print('sing')
        time.sleep(1)


def dance():
    for i in range(5):
        print('dance')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前线程数：', length)
        print(threading.enumerate())
        if length <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
