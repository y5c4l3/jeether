set debuginfod enabled on
set print thread-events
source /workspaces/cpython/Tools/gdb/libpython.py

# break _threadmodule.c:452
# break iobase.c:296
# break pylifecycle.c:2085
# run
# break _threadmodule.c:505

break _Py_Finalize
break ThreadHandle_join
run
