# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:

sensorInputPin = 2      # The voltage outputted from the photosensor
outputPin = 4           # The concentration outputted



# Pin Setup:
GPIO.setmode(GPIO.BCM)                  # Broadcom pin-numbering scheme
GPIO.setup(sensorInputPin, GPIO.IN)     # sensor pin set as input
GPIO.setup(outputPin, GPIO.OUT)            # PWM pin set as output

# Initial state for output:
GPIO.output(outputPin, GPIO.LOW)

# Code goes here:
