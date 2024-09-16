import io
import threading
import atexit

def process():
    while True:
        pass

t1 = threading.Thread(target=process, daemon=True)
t1.start()
atexit.register(lambda: t1.join())

