from machine import Pin
from time import sleep

# Ampel-LED
green_led = Pin(32, Pin.OUT)
yellow_led = Pin(33, Pin.OUT)
red_led = Pin(25, Pin.OUT)

# Fußgänger-LED
walk_green = Pin(14, Pin.OUT)
walk_red = Pin(12, Pin.OUT)

def car_green():
    green_led.on()
    yellow_led.off()
    red_led.off()

    walk_green.off()
    walk_red.on()

def pedestrian_green():
    # Übergang von Auto grün zu Auto rot
    green_led.off()
    yellow_led.on()
    red_led.on()
    sleep(0.3)

    yellow_led.off()
    sleep(0.1)

    # Fußgänger bekommen grün
    walk_green.on()
    walk_red.off()
    sleep(2)

    # Fußgänger bekommen rot
    walk_green.off()
    walk_red.on()
    sleep(0.2)

    # Auto Übergang von rot zu grün
    red_led.off()
    sleep(0.01)
    yellow_led.on()
    sleep(0.05)
    yellow_led.off()
    green_led.on()

def traffic_light(command):
    if command == '':
        car_green()
    elif command == 'walk':
        pedestrian_green()

        penis