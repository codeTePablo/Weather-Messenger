import os
import time
from dotenv import load_dotenv

from ui import Interface


class Main:
    """
    Main class to execute Interface
    """

    # st = time.time()  #  time to execute script
    # st_cpu_time = time.process_time()  #  CPU time of code

    ui = Interface()

    # et = time.time()
    # et_cpu_time = time.process_time()  #  CPU time of code
    # elapsed_time = et - st
    # res_cpu = et_cpu_time - st_cpu_time
    # print(elapsed_time, "seconds of time to execute script")
    # print(res_cpu, "seconds of CPU time")
