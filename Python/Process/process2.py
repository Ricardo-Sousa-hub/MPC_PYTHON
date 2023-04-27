# example of extending the Process class

from time import sleep
from multiprocessing import Process


# custom process class
class CustomProcess(Process):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print('This is coming from another process')


# entry point
if __name__ == '__main__':
    # create the process
    process = CustomProcess()
    # start the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process to finish')
    process.join()