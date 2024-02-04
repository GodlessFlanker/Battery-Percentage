import psutil
from plyer import notification
import time
import os
import sys

battery = psutil.sensors_battery()
while True:
    percent = battery.percent
    notification.notify(
        title="Battery Percentage",
        message= "%"+ str(percent)+" battery left.",
        timeout=10
    )
    if battery.percent == 50:
        
        print("Battery left 50 percent")
    time.sleep(60*60)
    continue