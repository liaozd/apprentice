import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'{self.name} @ {i}')


if __name__ == '__main__':
    t = MyThread()
    t.start()
