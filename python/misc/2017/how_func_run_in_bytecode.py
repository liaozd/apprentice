# -*- coding: utf-8 -*
# Python函数如何以字节码运行

import dis
sorted()


def add(a):
    a += 1


def subtract(a):
    a -= 1


if __name__ == '__main__':
    dis.dis(add)
    print()
    dis.dis(subtract)
