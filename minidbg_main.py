'''
Created on 11-Apr-2022

@author: dakshita
'''
import os
import sys 
from ctypes import *
import minidbg_debugger
from minidbg_debugger import debugger
from ptrace import syscall, debugger, binding
from ptrace.binding.func import PTRACE_TRACEME
import ptrace

ADDR_NO_RANDOMIZE = 0x0040000
libc = CDLL("libc.so.6")
libc.ptrace.argtypes = [c_uint64, c_uint64, c_void_p, c_void_p]
libc.ptrace.restype = c_uint64
personality = libc.personality
personality.restype = c_int
personality.argtypes = [c_ulong]

def execute_debugee(progname):    
    if ptrace(PTRACE_TRACEME, 0, 0, 0) < 0:
        sys.stderr.write("error in ptrace")
    return 
    os.execl(progname, progname, None)
                                             # how to pass string using ctypes
if __name__ == '__main__':
    count = len(sys.argv)                                               #to replace argc since linux doesnt have it
    if count<2:
        sys.stderr.write("Program name not specified")
    exit
    prog = sys.argv[1]
    pid = os.fork()

    if pid == 0:                                                        #child
        personality(ADDR_NO_RANDOMIZE)
        execute_debugee(prog)
    elif pid >= 1:                                                      #parent
        sys.stdout.write("started debugging process:  %s" %pid)
        sys.stdout.write("\n")
        dbg = debugger(prog, pid)
        dbg.run()
        