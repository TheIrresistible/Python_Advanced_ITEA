import time
import random


def repeater(repeats):

    def time_decorator(func):

        def wraper(*args):
            start_time = time.time()
            print('Function is wrapping')
            for i in range(repeats):

                print(func(*args))
            print('Function is wrapped')
            end_time = time.time()
            execution_time = end_time - start_time
            print(f'Function {func.__name__} has been {repeats}')
            print('Time has passed = ', execution_time)
        return wraper

    return time_decorator


@repeater(10)
def multiply(n, m):
    n += random.randint(1, 11)
    return n * m

multiply(1, 2)


