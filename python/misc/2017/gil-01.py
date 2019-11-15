import time
from threading import Thread


def counter1():
    for i in range(100000000):
        i = i + 1
    print 'this is i: {}'.format(i + 5)


def counter2():
    for j in range(100000000):
        j = j + 1
    print 'this is j: {}'.format(j + 10)


def counter1_sleep():
    for i in range(1000):
        i = i + 1
        time.sleep(0.01)
    print 'this is i: {}'.format(i + 5)


def counter2_sleep():
    for j in range(1000):
        j = j + 1
        time.sleep(0.01)
    print 'this is j: {}'.format(j + 10)


def main():
    # Not sleep
    start_time = time.time()
    for x in range(2):
        counter1()
        counter2()
    end_time = time.time()
    print 'Sequential Total time: {}\n'.format(end_time - start_time)

    start_time = time.time()
    for x in range(2):
        t1 = Thread(target=counter2)
        t2 = Thread(target=counter1)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    end_time = time.time()
    print '2 Threads Total time: {}\n'.format(end_time - start_time)

    # With sleep:
    print '\nWith Sleep(0.01) in func'
    start_time = time.time()
    for x in range(2):
        counter1_sleep()
        counter2_sleep()
    end_time = time.time()
    print 'Sequential With Sleep Total time: {}\n'.format(end_time - start_time)

    start_time = time.time()
    for x in range(2):
        t1 = Thread(target=counter2_sleep)
        t2 = Thread(target=counter1_sleep)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    end_time = time.time()
    print '2 Threads with sleep Total time: {}\n'.format(end_time - start_time)


if __name__ == '__main__':
    main()
