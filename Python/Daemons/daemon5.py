"""
processes can have children but a daemon process tt is not
Only one of rows (38 or 39) them have belong to the code
i, row 38) creating a process from a daemon process
process = Process(target=task1, daemon=True)
ii, row 39)  creating a not daemon process
process = Process(target=task1)
"""
from time import sleep
from multiprocessing import current_process
from multiprocessing import Process


# function to be executed by second daemon process
def task2():
    # get the current process
    process = current_process()
    # report if daemon process
    print(f'Daemon process 2: {process.daemon}')


# function to be executed in a new process
def task1():
    # get the current process
    process = current_process()
    # report if daemon process
    print(f'Daemon process 1: {process.daemon}')
    # create a new process
    try:
        process2 = Process(target=task2)
        # start the new process
        process2.start()
    except:
        print("daemonic processes are not allowed to have children")



# entry point
if __name__ == '__main__':
    # create a new daemon process
    process = Process(target=task1, daemon=True)
    # process = Process(target=task1)
    # start the new process
    process.start()
    # block for a moment to let the daemon process run
    process.join()