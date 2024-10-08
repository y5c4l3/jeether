import io
import threading
from spawner import ModuleSpawnerIO

class SpawnerIO(io.RawIOBase):
    def __init__(self):
        self.task = threading.Thread(target=self._process, daemon=True)
        self.task.start()
    def _process(self):
        while True:
            pass
    def readable(self):
        return True
    def close(self):
        print('finalizing...')
        self.task.join()

# exit as expected, finalizer is not called
# r = io.BufferedReader(SpawnerIO())

# stuck
r = io.BufferedReader(ModuleSpawnerIO())
