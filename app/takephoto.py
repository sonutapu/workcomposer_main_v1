import time
import pyscreenshot
from datetime import datetime , timedelta
from pathlib import Path
import os
from .models import Logtable_time

def takephoto():
    while True:
        directory="/Screenshots"
        cwd = os.getcwd()
        print(cwd)
        datetimeNow = datetime.now()
        datetimeString =datetimeNow.strftime("%d-%m-%Y %H-%M-%S")
        fileName = (f"screenshort-{datetimeString}.png")
        image =pyscreenshot.grab()
        # ennn = Logtable_time(screenshot=image)
        # ennn.save()
        if (os.path.exists("Screenshots") == False):
            cur_dir=Path.cwd()
            #cwd = os.getcwd()
            csv_path=str(cur_dir)+"/Screenshots"
        # if not os.path.exists(directory):
        #     os.makedirs(directory)
        #     os.chdir(directory)
        #     # datetimeNow = datetime.now()
        #     # datetimeString =datetimeNow.strftime("%d-%m-%Y %H-%M-%S")
        #     # fileName = (f"screenshort-{datetimeString}.png")
        #     # image =pyscreenshot.grab()
            image.save(csv_path)
        else:
            cur_dir=Path.cwd()
            csv_path=str(cur_dir)+"/Screenshots"
            # os.chdir(directory)
            # # datetimeNow = datetime.now()
            # # datetimeString =datetimeNow.strftime("%d-%m-%Y %H-%M-%S")
            # # fileName = (f"screenshort-{datetimeString}.png")
            
            image.save(csv_path)
        time.sleep(5)




















