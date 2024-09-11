import gzip

mode = 'rb'
threads = 2
test_file = "test.gz"
with open(test_file, "wb") as f:
    f.write(gzip.compress(b"test" * (10 * 1024 * 1024)))
with open('test_threaded.sample.py', "wt") as f:
    f.write("from zlib_ng import gzip_ng_threaded\n")
    f.write(
        f"f = gzip_ng_threaded.open('{test_file}', "
        f"mode='{mode}', threads={threads})\n"
    )
    f.write("raise Exception('Error')\n")
