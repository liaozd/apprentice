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


# https://foofish.net/python-decorator.html
def user_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            msg = '{} is running'.format(func.__name__)
            if level == 'warning':
                print(msg)
            else:
                print(msg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@user_logging(level='warning')
def foo(name='foo'):
    print('I am {}'.format(name))


# retries: https://juejin.im/post/5c036f906fb9a04a006ec0b9
def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _time in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_rasied = e
            raise last_rasied

        return wrapper

    return decorator


@retry(times=2)
def wrong_func():
    print('wrong_func is running.')
    print(1 / 0)


wrong_func()
