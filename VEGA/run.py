

import multiprocessing
import subprocess     # Remove if not used
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Change working directory to VEGA root

from main import start  # Move imports to the top if possible
from engine.features import hotword

# To run Vega
def startVega():
        # Code for process 1
        print("Process 1 is running.")
        start()

# To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        hotword()

# Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startVega)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")
