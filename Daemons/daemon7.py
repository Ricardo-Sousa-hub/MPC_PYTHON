"""
A daemon run within the program that it is started
example:
Only one of rows (32 or 33) them have belong to the code
i, row 32) if we defined process = Process(target=task, daemon=True) as a daemon
the task that it is run ended when the program paren t is ended because the process
is end in that momment.
ii, ows 33) if we defined process = Process(target=task) as not a daemon
the task that it is run out of the program where it is started. Then the task that is run
within the process continued doing its wor
"""
from time import sleep
from multiprocessing import current_process
from multiprocessing import Process


# function to be executed in a new process
def task():
    # get the current process
    process = current_process()
    # report if daemon process
    print(f'Daemon process: {process.daemon}')
    # loop for a while
    for i in range(1000):
        print(i, flush=True)
        # block for a moment
        sleep(0.1)


# entry point
if __name__ == '__main__':
    # create a new daemon process
    process = Process(target=task, daemon=True)
    #process = Process(target=task)
    # start the new process
    process.start()
    # block for a moment to let the daemon process run
    sleep(3)
    # prepare the user
    print('Main process exiting...')