# example of changing the current process to be a daemon process

from multiprocessing import current_process
# get the current process
process = current_process()
# report if daemon process
print(f'Daemon process: {process.daemon}')
# try and change the current process to be a daemon
process.daemon = True
# report if daemon process
print(f'Daemon process: {process.daemon}')