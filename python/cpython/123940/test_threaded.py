# import os, sys
# sys.path.insert(0, os.path.abspath('./python-zlib-ng/src'))

import zlib_ng
print(zlib_ng.__path__)

from zlib_ng import gzip_ng_threaded
f = gzip_ng_threaded.open('test.gz', mode='rb', threads=1)
# f.close()
raise Exception('Error')
