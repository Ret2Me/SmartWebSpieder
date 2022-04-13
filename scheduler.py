import logging
import psutil
import json
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import config

scheduler = BackgroundScheduler()
logging.getLogger('apscheduler.executors.default').propagate = False

@scheduler.scheduled_job(trigger="interval", name="hardware_monitor",  minutes=config.HARDWARE_SCAN_INTERVAL)
def hardware_monitor():
    """ Log information about RAM, CPU and DISK usage. """
    file = open('./logs/hardware/hardware.json', 'r+')
    if file.closed:
        return

    hardware_logs = []
    if len(file.read()) != 0:
        file.seek(0)
        hardware_logs = json.load(file)


    # add information about hardware usage where key is actual date time and value array of cpu, ram and disk usage
    # pop the oldest element and append new information about hardware usage
    date = datetime.now()
    try:
        hardware_logs.append({'DATE': f'{date.year},{date.month},{date.day},'
                                      f'{date.hour},{date.minute},{date.second}',
                              'CPU': str(psutil.cpu_percent()),
                              'RAM': str(psutil.virtual_memory().percent),
                              'DISK': str(psutil.disk_usage(config.DISK_MONITORING_PATH).percent)})

        if len(hardware_logs) == config.MONITORING_LOGS_LENGTH + 1:
            hardware_logs.pop(0)
    except:
        file.close()
        return

    # trunk file before dumping array
    file.seek(0)
    file.truncate(0)

    json.dump(hardware_logs, file)
    file.close()


scheduler.start()
