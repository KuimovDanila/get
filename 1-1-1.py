import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
GPIO.input(21)
GPIO.output(24, GPIO.input(21))



