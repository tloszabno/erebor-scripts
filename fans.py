#!/usr/bin/env python

import RPi.GPIO as GPIO
from subprocess import check_output
from time import sleep


UPPER_TEMP_LEVEL = 65.0
LOWER_TEMP_LEVEL = 55.0
FAN_CONTROL_PIN_NUMBER = 40
SLEEP_INTERVAL = 10
EX_FAN_CONTROL_PIN_NUMBER = 37

def get_cpu_temp():
    def __get_temp__internal():
        out = check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
        return float(out.split('=')[1].split('\'')[0])
    try:
        t1 = __get_temp__internal()
        t2 = __get_temp__internal()
        return t1 if t1 < t2 else t2
    except:
        return None


def turn_off_fan():
    GPIO.output(FAN_CONTROL_PIN_NUMBER, False)
    GPIO.output(EX_FAN_CONTROL_PIN_NUMBER, False)


def turn_on_fan():
    GPIO.output(FAN_CONTROL_PIN_NUMBER, True)
    GPIO.output(EX_FAN_CONTROL_PIN_NUMBER, True)


def setup_fan():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FAN_CONTROL_PIN_NUMBER, GPIO.OUT)
    GPIO.output(FAN_CONTROL_PIN_NUMBER, False)

    GPIO.setup(EX_FAN_CONTROL_PIN_NUMBER, GPIO.OUT)
    GPIO.output(EX_FAN_CONTROL_PIN_NUMBER, False)


def main():
    fan_on = False
    setup_fan()
    while True:
        temp = get_cpu_temp()
        if temp:
            if fan_on and temp < LOWER_TEMP_LEVEL:
                turn_off_fan()
                fan_on = False
            if (not fan_on) and temp > UPPER_TEMP_LEVEL:
                turn_on_fan()
                fan_on = True
        # if unknow state turn on fan
        elif not fan_on:
            turn_on_fan()
            fan_on = True
        sleep(SLEEP_INTERVAL)


sleep(SLEEP_INTERVAL)
main()

