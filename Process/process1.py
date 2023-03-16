# example of running a function with arguments in another process

from time import sleep
from multiprocessing import Process


# a custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)


# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task, args=(1.5, 'New message from another process'))
    # run the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()