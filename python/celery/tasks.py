import time
import sys
from celery import *
from celery.result import allow_join_result

app = Celery('tasks', backend='redis://localhost:6379/1//', broker='redis://localhost:6379//')


@app.task
def add(x):
    print(x)
    time.sleep(3)
    return x


# @app.task
# def group1():
#     return group([add.s(2, 2), add.s(4, 4),])

# @app.task
# def group2():
#     return group([add.s(2, 2), add.s(4, 4),])


@app.task
def init_hosts(input):
    func_name = sys._getframe().f_code.co_name
    for i in range(3):
        print(func_name + ': ' + add(str(i)))
    return input


@app.task
def install_hosts(input):
    func_name = sys._getframe().f_code.co_name
    for i in range(3):
        print(func_name + ': ' + add(str(i)))
    return input


@app.task
def boot_hosts(input):
    func_name = sys._getframe().f_code.co_name
    print(func_name)


@app.task
def big_job():
    init_hosts()
    install_hosts()


# GROUPS
# results = group(init_hosts.s('s'), install_hosts.s('b'))
# results().get()

# CHAINS
# results = chain(init_hosts.s('s'), install_hosts.s(), boot_hosts.s())
# results().get()

# CHAINS GROUP
# c3 = (group(add.s(i, i) for i in xrange(10)) | xsum.s())

print('--- Buttom Line ---')
