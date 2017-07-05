#!/usr/bin/env python

# https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=227s


def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print('Wrapper Excuted this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper


# normal format
def display():
    print('Display function ran')
decorated = decorator_function(display)
decorated()


# decorator format
@decorator_function
def decorator_display():
    print('Decorator display function ran')
decorator_display()


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
