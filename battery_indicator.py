"""
Battery Level Notifier App
Author: Ankit Kundariya (https://github.com/AnkitKundariya/)
License: MIT
"""

import gi
import psutil

gi.require_version("Notify", "0.7")
from gi.repository import Notify
import time


def battery_notification():
    battery = psutil.sensors_battery()
    if battery.percent > 90 and battery.power_plugged:
        message = f"Battery level is {battery.percent}% and charging. Unplug to protect battery."
        notification = Notify.Notification.new("Battery Alert", message)
        notification.show()
    elif battery.percent < 30 and not battery.power_plugged:
        message = f"Battery level is {battery.percent}% and charging. Plug to avoid system shutdown."
        notification = Notify.Notification.new("Battery Alert", message)
        notification.show()


def main():
    Notify.init("Battery Notifier")

    while True:
        battery_notification()
        time.sleep(10)  # Check every 60 seconds


if __name__ == "__main__":
    main()
