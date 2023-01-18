from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .job import  schedule_api 

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(schedule_api,'interval',seconds=1)
    scheduler.start()

def stop():
    scheduler=BackgroundScheduler()
    scheduler.shutdown()
