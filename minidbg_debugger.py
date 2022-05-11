'''
Created on 11-Apr-2022

@author: dakshita
'''
from ctypes import *
import sys
import os
import readline
import rlcompleter
from ptrace.binding.func import PTRACE_TRACEME, PTRACE_CONT
import ptrace


global f
global options 

class debugger():
    def __init__(self, progname, pid):
        self.progname = progname             #            m_elf = elf::elf{elf::create_mmap_loader(fd)};
        self.pid= pid
        f = os.fdopen(os.open(progname, os.O_RDONLY))
    def continue_exec(self):
        ptrace(PTRACE_CONT, self.pid, None,None)
        os.waitpid(self.pid, options)
        
    def handle_command(self, line):
        self.line = line
        args = line.split()
        command = args[0]
        if command.startswith('continue'):
            self.continue_exec()
        else:
            sys.stderr.write("unknown command")
            sys.stdout.write("\n")
            
    def run(self):
        options = 0
        os.waitpid(self.pid, options)
        line = f.readline()        #       wait_for_signal();      initialise_load_address();
        while line is not None:
            self.handle_command(line)
            f.readline.add_history(line)
            f.readline.free(line)
            
