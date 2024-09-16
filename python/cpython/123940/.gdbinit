set debuginfod enabled on
set print thread-events

source ~/projects/@contributions/python/cpython/Tools/gdb/libpython.py

#break _Py_Finalize
break Py_FinalizeEx

run

break thread_run
command
    echo Thread Run exiting: 
    print &handle->thread_is_exiting
    continue
    end

break _PyEvent_Notify
command
    bt
    echo Event Fired: 
    print evt
    continue
    end

break detach_thread
command
    # bt
    continue
    end

break Py_EndInterpreter
command
    echo End Interpreter\n
    continue
    end

break _PyRuntime_Finalize
command
    echo Runtime Finalize\n
    continue
    end

break _PyRuntimeState_Fini
command
    echo Runtime State Fini\n
    continue
    end

break ThreadHandle_join thread 1
break _PyEvent_Notify thread 2

break _PyRuntimeState_ReInitThreads

break take_gil thread 2
command
    echo TAKE GIL\n
    # bt
    # bt
    continue
    end
break drop_gil thread 2
command
    echo DROP GIL\n
    # bt
    # continue
    end

break _PyEvent_Notify thread 2

# break ceval_gil.c:294 thread 2

# break _PyEvent_Notify
# break _threadmodule.c:361

# break _PyErr_Clear
# break _threadmodule.c:341
