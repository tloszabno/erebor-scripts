#!/usr/bin/env python

import RPi.GPIO as GPIO
from subprocess import check_output
from time import sleep

FAN_CONTROL_PIN_NUMBER = 37

TURN_ON_FOR_SEC = 2 * 60
TURN_OFF_FOR_SEC = 30 * 60


def turn_off_fan():
    print("Turn off fan")
    GPIO.output(FAN_CONTROL_PIN_NUMBER, False)


def turn_on_fan():
    print("Turn on fan")
    GPIO.output(FAN_CONTROL_PIN_NUMBER, True)


def setup_fan():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FAN_CONTROL_PIN_NUMBER, GPIO.OUT)
    GPIO.output(FAN_CONTROL_PIN_NUMBER, False)

def main():
    setup_fan()
    while True:
        turn_on_fan()
        sleep(TURN_ON_FOR_SEC)
        turn_off_fan()
        sleep(TURN_OFF_FOR_SEC)

main()
