from pynput.mouse import Listener
import logging
import os
from pathlib import Path

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
try:
    if (os.path.exists("mouseclick-log.csv") == False):
        cur_dir=Path.cwd()
        #cwd = os.getcwd()
        csv_path=str(cur_dir)+"/mouseclick-log.csv"
        logging.basicConfig(filename=csv_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    else:
        print("File Exists")
        cur_dir=Path.cwd()
        csv_path=str(cur_dir)+"/mouseclick-log.csv"
        logging.basicConfig(filename=csv_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
except:
    print("ERROR IN CREATING .CSV FILE")       
with Listener(on_click=on_click) as listener:
    listener.join()