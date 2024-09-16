import io
import threading
import atexit

def process():
    while True:
        pass

def on_exit():
    t1 = threading.Thread(target=process, daemon=True)
    t1.start()
    t1.join()

# Related to:
# https://github.com/python/cpython/issues/113964
# https://github.com/python/cpython/pull/116982
# https://github.com/python/cpython/pull/116677
atexit.register(on_exit)