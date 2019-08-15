import threading
import time


def hello_world():
    print("sleep 1")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(4):
        t = threading.Thread(target=hello_world)
        t.start()
