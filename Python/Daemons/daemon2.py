# example of change a process created to a daemon process

from multiprocessing import Process, Manager
process = Process()
# configure the process to be a daemon process
process.daemon = True
print(f'Daemon process: {process.daemon}')