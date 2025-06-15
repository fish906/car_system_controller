from machine import Pin
from time import sleep
from datetime import datetime

green_led = Pin(32, Pin.OUT)
yellow_led = Pin(33, Pin.OUT)
red_led = Pin(25, Pin.OUT)

walk_green = Pin(14, Pin.OUT)
walk_red = Pin(12, Pin.OUT)

walk_button = Pin(13, Pin.IN, Pin.PULL_UP)
time_stamp = datetime.now().strftime('%H:%M:%SUhr')

def normal_traffic():
    green_led.on()
    yellow_led.off()
    red_led.off()
    walk_green.off()
    walk_red.on()


def pedestrian_crossing():
    # changing to car yellow/red
    green_led.off()
    yellow_led.on()
    sleep(1.5)

    # change to car red
    yellow_led.off()
    red_led.on()
    sleep(0.8)

    # pedestrian green
    walk_green.on()
    walk_red.off()
    sleep(3)

    # change to pedestrian red
    walk_green.off()
    walk_red.on()
    sleep(0.8)

    # changing from car red to car yellow
    red_led.off()
    yellow_led.on()
    sleep(0.8)

    # changing from car yellow to car green
    yellow_led.off()
    green_led.on()
    print(f'{time_stamp} - Cycle completed!\n')

normal_traffic()

while True:
    if walk_button.value() == 0:
        print(f'{time_stamp}: Pedestrian Crossing initiated!')
        pedestrian_crossing()
        sleep(0.3)

    else:
        normal_traffic()
