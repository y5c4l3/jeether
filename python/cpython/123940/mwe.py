import threading
import time
import queue
import io
import gzip

from zlib_ng import zlib_ng

class SpawnerIO(io.RawIOBase):
    def __init__(self):
        self.raw = open('test.gz', 'rb')
        self.reader = zlib_ng._GzipReader(self.raw, 8 * 1024 * 1024)
        self.running = True
        self.queue = queue.Queue(2)
        self._closed = False
        self.task = threading.Thread(target=self.process, daemon=True)
        self.task.start()
    def _check_closed(self, msg=None):
        if self._closed:
            raise ValueError("I/O operation on closed file")
    def process(self):
        while self.running:
            data = self.reader.read(1024 * 1024)
            if not data:
                break
            while self.running:
                try:
                    self.queue.put(data)
                    break
                except:
                    pass
        print("done")
    def close(self):
        print("close")
        print(self.task.is_alive())
        self.running = False
        print(self.task.is_alive())
        self.task.join()
        print("join done")
    @property
    def closed(self) -> bool:
        return self._closed

spawner = SpawnerIO()

raise Exception("1")
