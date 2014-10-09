#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) # Step (Floppy Pin 20)
GPIO.setup(17, GPIO.OUT) # Direction (Floppy Pin 18)
GPIO.setup(24, GPIO.OUT) # Write (Floppy Pin 22)
print("Turning on")
GPIO.output(17, GPIO.HIGH) # Go one direction
time.sleep(.005)
for num in range(1, 75):
    GPIO.output(18, GPIO.HIGH) # Step
    time.sleep(.004)
    GPIO.output(24, GPIO.HIGH) # Write
    time.sleep(.004)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
GPIO.output(17, GPIO.LOW) # Go the opposite direction
time.sleep(.005)
for num in range(1, 75):
    GPIO.output(18, GPIO.HIGH) # Step
    time.sleep(.004)
    GPIO.output(24, GPIO.HIGH) # Write
    time.sleep(.004)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
time.sleep(1)
print("Exiting")
GPIO.cleanup()
