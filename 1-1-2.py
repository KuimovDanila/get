import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.IN)
GPIO.setup(16, GPIO.OUT)

a=GPIO.input(21)
GPIO.output(16,1)
        

