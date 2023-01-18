import time
# import winsound
from ctypes import Structure, windll, c_uint, sizeof, byref
from datetime import datetime,timedelta
import os
from pathlib import Path
import pandas as pd
import csv


# file=open("E:\Mouse-idleTime\idletime.csv",'w',newline='')

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():  
    
    lastInputInfo = LASTINPUTINFO()            
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    # print ("%d:%d:%d" % (hours, minutes, seconds))
    data="%d:%d:%d" % (hours, minutes, seconds)
    return [seconds,data]
   
lst = []
data={}
while True:
    GetLastInputInfo =get_idle_duration()
    if GetLastInputInfo[0]:
        now = datetime.now()
        last_idle_time = now.strftime("%H:%M:%S")
        # print("Last idle timing :", last_idle_time)
        data={'LAST_IDLE_TIME':last_idle_time}
        print(data)
#         try:
#             if (os.path.exists("mouseidle.csv") == False):
#                 cur_dir=Path.cwd()
#                 #cwd = os.getcwd()
#                 csv_path=str(cur_dir)+"/mouseidle.csv"
# ############CREATING DATAFRAME   ##################################
#                 items = data.items()
#                 dfs=pd.DataFrame({'keys': [i[0] for i in items], 'values': [i[1] for i in items]})
#                 newdf = dfs.drop_duplicates()
#                 print(dfs)
#                 newdf.to_csv(csv_path, mode='a', index=False, header=False)
#             else:
#                 print("File Exists")
#                 cur_dir=Path.cwd()
#                 csv_path=str(cur_dir)+"/mouseidle.csv"
# ############CREATING DATAFRAME  ##########################################
#                 items = data.items()
#                 dfs=pd.DataFrame({'keys': [i[0] for i in items], 'values': [i[1] for i in items]})
#                 newdf = dfs.drop_duplicates()
#                 # print(dfs)
#                 newdf.to_csv(csv_path, mode='a', index=False, header=False)
#         except:
#             print("ERROR IN CREATING .CSV FILE")
        lst.append(GetLastInputInfo[1])
        
######### Converting the second to minutes and hours  ####################        
    second=len(lst)
    total_idle_time = timedelta(seconds =second)
    # print('total_idle_time',total_idle_time)
################### CREATING CSV FILE IN DIRECTORY #########################
    data={'TOTAL_IDLE_TIME':total_idle_time}
    # print(data)
    try:
        if (os.path.exists("mouseidle.csv") == False):
            cur_dir=Path.cwd()
            #cwd = os.getcwd()
            csv_path=str(cur_dir)+"/mouseidle.csv"
            file=open("mouseidle.csv",'w')
            file.write(str(total_idle_time))
#############CREATING DATAFRAME  ######################################
#             items = data.items()
#             dfs=pd.DataFrame({'keys': [i[0] for i in items], 'values': [i[1] for i in items]})
#             print(dfs)
#             newdf = dfs.drop_duplicates()
#             newdf.to_csv(csv_path, mode='a', index=False, header=False)
        else:
            print("File Exists")
            cur_dir=Path.cwd()
            csv_path=str(cur_dir)+"/mouseidle.csv"
            file=open("mouseidle.csv",'w')
            file.write(str(total_idle_time))
############CREATING DATAFRAME  #####################################
            # items = data.items()
            # dfs=pd.DataFrame({'keys': [i[0] for i in items], 'values': [i[1] for i in items]})
            # print(dfs)
            # newdf = dfs.drop_duplicates()
            # newdf.to_csv(csv_path, mode='a', index=False, header=False)       
    except:
        print("ERROR IN CREATING .CSV FILE") 
########################### GIVING  A SOUND NOTIFICATION ############

    # if GetLastInputInfo == 120:
    #     sound = r"c:\windows\media\notify.wav"
    #     winsound.PlaySound(sound, winsound.SND_FILENAME)

    # if GetLastInputInfo == 180:
    #     sound = r"c:\windows\media\ringout.wav"
    #     winsound.PlaySound(sound, winsound.SND_FILENAME)
    #     winsound.PlaySound(sound, winsound.SND_FILENAME)
    #     winsound.PlaySound(sound, winsound.SND_FILENAME)
    time.sleep(1)