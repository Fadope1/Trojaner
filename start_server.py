"""Create multiprocessing instances for each job"""

import Server

from multiprocessing import Process


if __name__ == '__main__':
    cmd_process = Process(Server)
    cmd_process.start()
    cmd_process.join()
