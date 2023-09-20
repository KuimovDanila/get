import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setup(dac, GPIO.OUT)
for i in range(8):
    GPIO.output(dac[i], number[i])
time.sleep(10)
GPIO.output(dac, 0)
GPIO.cleanup()
import matplotlib.pyplot as plt
import numpy as np
a =[255, 127, 64, 32, 5, 0]
b =[3.24, 1.67, 0.86, 0.45, 0.11, 0.04]
plt.plot(a, b)
plt.show()