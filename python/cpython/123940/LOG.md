# Trace

```
(gdb) r
Starting program: /usr/local/bin/python3 test_threaded.py
warning: Error disabling address space randomization: Operation not permitted
Downloading separate debug info for system-supplied DSO at 0x7ffc1a128000
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
['/usr/local/lib/python3.14/site-packages/zlib_ng']
[New Thread 0x7b558a18e6c0 (LWP 1205096)]
Traceback (most recent call last):
  File "/workspaces/cpython/jeether/python/cpython/123940/test_threaded.py", line 10, in <module>
    raise Exception('Error')
Exception: Error
[Thread 0x7b558a18e6c0 (LWP 1205096) exited]
?
^C
Thread 1 "python3" received signal SIGINT, Interrupt.
Downloading source file /builddir/build/BUILD/glibc-2.39/nptl/futex-internal.c
0x00007b5598d67919 in __futex_abstimed_wait_common64 (private=<optimized out>, futex_word=0x7ffc1a00c240, expected=0, op=393, abstime=0x0,
    cancel=true) at futex-internal.c:57
warning: 57     futex-internal.c: No such file or directory
(gdb) backtrace
#0  0x00007b5598d67919 in __futex_abstimed_wait_common64 (private=<optimized out>, futex_word=0x7ffc1a00c240, expected=0, op=393, abstime=0x0,
    cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x7ffc1a00c240, expected=expected@entry=0, clockid=clockid@entry=0,
    abstime=abstime@entry=0x0, private=<optimized out>, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007b5598d6799f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x7ffc1a00c240, expected=expected@entry=0,
    clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=<optimized out>) at futex-internal.c:139
#3  0x00007b5598d7338f in do_futex_wait (sem=sem@entry=0x7ffc1a00c240, abstime=0x0, clockid=0)
    at /builddir/build/BUILD/glibc-2.39/nptl/sem_waitcommon.c:111
#4  0x00007b5598d73428 in __new_sem_wait_slow64 (sem=sem@entry=0x7ffc1a00c240, abstime=0x0, clockid=0)
    at /builddir/build/BUILD/glibc-2.39/nptl/sem_waitcommon.c:183
#5  0x00007b5598d734ad in __new_sem_wait (sem=sem@entry=0x7ffc1a00c240) at sem_wait.c:42
#6  0x0000000000697151 in _PySemaphore_PlatformWait (sema=0x7ffc1a00c240, timeout=-1) at Python/parking_lot.c:142
#7  _PySemaphore_Wait (sema=sema@entry=0x7ffc1a00c240, timeout=timeout@entry=-1, detach=detach@entry=1) at Python/parking_lot.c:213
#8  0x0000000000697380 in _PyParkingLot_Park (addr=addr@entry=0x1567f99, expected=expected@entry=0x7ffc1a00c2cf, size=size@entry=1,
    timeout_ns=timeout_ns@entry=-1, park_arg=park_arg@entry=0x0, detach=detach@entry=1) at Python/parking_lot.c:316
--Type <RET> for more, q to quit, c to continue without paging--
#9  0x000000000069010d in PyEvent_WaitTimed (evt=evt@entry=0x1567f99, timeout_ns=timeout_ns@entry=-1, detach=detach@entry=1) at Python/lock.c:290
#10 0x000000000074b650 in ThreadHandle_join (self=0x1567f60, timeout_ns=-1) at ./Modules/_threadmodule.c:505
#11 0x000000000074bc99 in PyThreadHandleObject_join (self=0x7b558af9b2d0, args=<optimized out>) at ./Modules/_threadmodule.c:642
#12 0x00000000004c6b0d in method_vectorcall_VARARGS (func=0x7b558b136a50, args=0x7b5598fa80f8, nargsf=<optimized out>, kwnames=<optimized out>)
    at Objects/descrobject.c:324
#13 0x00000000004b84c7 in _PyObject_VectorcallTstate (tstate=0xa04b90 <_PyRuntime+328912>, callable=0x7b558b136a50, args=0x189,
    nargsf=9223372036854775810, kwnames=0x0) at ./Include/internal/pycore_call.h:167
#14 0x000000000060f18a in _PyEval_EvalFrameDefault (tstate=0xa04b90 <_PyRuntime+328912>, frame=<optimized out>, throwflag=0)
    at Python/generated_cases.c.h:926
#15 0x00000000004b84c7 in _PyObject_VectorcallTstate (tstate=tstate@entry=0xa04b90 <_PyRuntime+328912>, callable=0x7b558aa52810, args=0x189,
    args@entry=0x45aa8e0b48f80, nargsf=nargsf@entry=1, kwnames=kwnames@entry=0x0) at ./Include/internal/pycore_call.h:167
#16 0x00000000004bab67 in PyObject_VectorcallMethod (name=<optimized out>, args=0x0, args@entry=0x7ffc1a00c6b8, nargsf=1,
    nargsf@entry=9223372036854775809, kwnames=kwnames@entry=0x0) at Objects/call.c:856
#17 0x000000000071db77 in PyObject_CallMethodNoArgs (self=0x7b558afd9310, name=<optimized out>) at ./Include/cpython/abstract.h:65
#18 _io__Buffered_close_impl (self=0x7b558aa52090) at ./Modules/_io/bufferedio.c:576
#19 _io__Buffered_close (self=0x7b558aa52090, _unused_ignored=<optimized out>) at ./Modules/_io/clinic/bufferedio.c.h:374
#20 0x00000000004c6ff6 in method_vectorcall_NOARGS (func=0x7b558af02c30, args=0x7ffc1a00c7d0, nargsf=<optimized out>, kwnames=<optimized out>)
    at Objects/descrobject.c:447
#21 0x00000000004b84c7 in _PyObject_VectorcallTstate (tstate=tstate@entry=0xa04b90 <_PyRuntime+328912>, callable=0x7b558af02c30, args=0x189,
    args@entry=0x45aa8e0b49098, nargsf=nargsf@entry=1, kwnames=kwnames@entry=0x0) at ./Include/internal/pycore_call.h:167
#22 0x00000000004bab67 in PyObject_VectorcallMethod (name=<optimized out>, args=0x0, args@entry=0x7ffc1a00c7d0, nargsf=1,
    nargsf@entry=9223372036854775809, kwnames=kwnames@entry=0x0) at Objects/call.c:856
#23 0x000000000071545e in PyObject_CallMethodNoArgs (self=0x7b558aa52090, name=<optimized out>) at ./Include/cpython/abstract.h:65
#24 iobase_finalize (self=0x7b558aa52090) at ./Modules/_io/iobase.c:315
#25 0x000000000051f7a0 in PyObject_CallFinalizer (self=0x7b558aa52090) at Objects/object.c:494
#26 PyObject_CallFinalizerFromDealloc (self=0x7b558aa52090) at Objects/object.c:512
#27 0x000000000071c117 in buffered_dealloc (self=0x7ffc1a00c240) at ./Modules/_io/bufferedio.c:415
#28 0x00000000005239cc in _Py_Dealloc (op=0x7b558aa52090) at Objects/object.c:2893
#29 0x000000000050c4b3 in Py_DECREF (lineno=459, op=0x7b558aa52090, filename=<optimized out>) at ./Include/refcount.h:351
#30 Py_XDECREF (op=0x7b558aa52090) at ./Include/refcount.h:459
#31 dictkeys_decref (interp=<optimized out>, dk=dk@entry=0x7b558afbdcf0, use_qsbr=false) at Objects/dictobject.c:458
#32 0x00000000005076c3 in dict_dealloc (self=0x7b558af65f10) at Objects/dictobject.c:3120
#33 0x00000000005239cc in _Py_Dealloc (op=0x7b558af65f10) at Objects/object.c:2893
--Type <RET> for more, q to quit, c to continue without paging--
#34 0x000000000051d75f in Py_DECREF (lineno=459, op=0x7b558af65f10, filename=<optimized out>) at ./Include/refcount.h:351
#35 Py_XDECREF (op=0x7b558af65f10) at ./Include/refcount.h:459
#36 module_dealloc (m=0x7b558af66690) at Objects/moduleobject.c:777
#37 0x00000000005239cc in _Py_Dealloc (op=0x7b558af66690) at Objects/object.c:2893


#38 0x000000000050387b in Py_DECREF (lineno=459, op=0x7b558af66690, filename=<optimized out>) at ./Include/refcount.h:351
#39 Py_XDECREF (op=0x7b558af66690) at ./Include/refcount.h:459
#40 insertdict (interp=0x9cdf28 <_PyRuntime+104552>, mp=0x7b558b0f4a70, key=0x7b558afdb510, hash=<optimized out>, value=<optimized out>)
    at Objects/dictobject.c:1781
#41 0x000000000049111c in PyObject_SetItem (o=0x7ffc1a00c240, o@entry=0x7b558b0f4a70, key=0x189, value=0x0) at Objects/abstract.c:232
#42 0x000000000069c8a3 in finalize_remove_modules (modules=0x7b558b0f4a70, verbose=0) at Python/pylifecycle.c:1559
#43 finalize_modules (tstate=tstate@entry=0xa04b90 <_PyRuntime+328912>) at Python/pylifecycle.c:1706
#44 0x000000000069b8b9 in _Py_Finalize (runtime=<optimized out>) at Python/pylifecycle.c:2085
#45 0x00000000006e7c0d in Py_RunMain () at Modules/main.c:777
#46 0x00000000006e8560 in pymain_main (args=args@entry=0x7ffc1a00ce48) at Modules/main.c:805
#47 0x00000000006e85d8 in Py_BytesMain (argc=<optimized out>, argv=0x189) at Modules/main.c:829
#48 0x00007b5598cff088 in __libc_start_call_main (main=main@entry=0x41e8b0 <main>, argc=argc@entry=2, argv=argv@entry=0x7ffc1a00cf98)
    at ../sysdeps/nptl/libc_start_call_main.h:58
#49 0x00007b5598cff14b in __libc_start_main_impl (main=0x41e8b0 <main>, argc=2, argv=0x7ffc1a00cf98, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7ffc1a00cf88) at ../csu/libc-start.c:360
#50 0x000000000041e7e5 in _start ()
```
