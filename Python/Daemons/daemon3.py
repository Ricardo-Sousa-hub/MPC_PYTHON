# example of checking if the current process is a daemon
# you can put it as a daemon process, row 7

from multiprocessing import current_process
# get the current process
process = current_process()
# process.daemon=True
# report if daemon process
print(f'Daemon process: {process.daemon}')