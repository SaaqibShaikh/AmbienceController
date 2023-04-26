#!/usr/bin/python
import struct
import time
import sys
import dbus
from threading import Thread, Lock

# Copy this file to /usr/bin as root
# Change permissions of this file to 754
# This file in /usr/bin should be owned by root, group is root

infile_path = "/dev/input/by-path/platform-i8042-serio-0-event-kbd"   # Keyboard events
TIMEOUT = 20                        # in seconds

mutex = Lock()
countdown = TIMEOUT

def kb_light_set(value):
    bus = dbus.SystemBus()
    kbd_backlight_proxy = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/KbdBacklight')
    kbd_backlight = dbus.Interface(kbd_backlight_proxy, 'org.freedesktop.UPower.KbdBacklight')
    kbd_backlight.SetBrightness(value)


def countdown_thread():
    global countdown
    while True:
         time.sleep(1)    # sleep for 1 second
         mutex.acquire()
         try:
             if countdown > 0:
                 countdown -= 1
                 if countdown == 0:
                     kb_light_set(0)   # turn off keyboard backlight
         finally:
             mutex.release()

kb_light_set(1)   # turn on keyboard backlight
t = Thread(target=countdown_thread)
t.start()

FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)   # are there any keyboard events?

while event:
    mutex.acquire()
    try:
        if countdown < 2:
            kb_light_set(1)    # turn on keyboard backlight
        countdown = TIMEOUT
    finally:
        mutex.release()
    event = in_file.read(EVENT_SIZE)   # are there any keyboard events?

in_file.close()