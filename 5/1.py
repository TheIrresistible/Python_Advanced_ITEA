from threading import Thread
from time import sleep


def threaded(fn):

    def wrapper(daemon, name, *args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs, name=name, daemon=daemon)
        thread.start()
        return thread
    return wrapper


@threaded
def io_bound(name, t):
    print(f'{name} operation started')
    sleep(t)
    print(f'{name} operation ended')


io_bound(True, '1', 'Google', 3)
io_bound(False, '2', 'Amazon', 2)
io_bound(False, '3', 'Reddit', 4)

