# example of creating two processes, a dameon and other that is not

from multiprocessing import Process

import multiprocessing.process
# create a new daemon process
process1 = Process(daemon=True)
process2 = Process()
# get the current process
# report if daemon process
print(f'Daemon process: {process1.daemon}')
print(f'Daemon process: {process2.daemon}')