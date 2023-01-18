from pynput.mouse import Listener
import logging
import os
from pathlib import Path


def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
try:
    if (os.path.exists("mouse_scroll.csv") == False):
        cur_dir=Path.cwd()
        #cwd = os.getcwd()
        csv_path=str(cur_dir)+"/mouse_scroll.csv"
        logging.basicConfig(filename=csv_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    else:
        print("File Exists")
        cur_dir=Path.cwd()
        csv_path=str(cur_dir)+"/mouse_scroll.csv"
        logging.basicConfig(filename=csv_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
except:
    print("ERROR IN CREATING .CSV FILE")

with Listener(on_scroll=on_scroll) as listener:
    listener.join()