import RPi.GPIO as GPIO
import time


# Pin definitions

pwmPin = 18
ledPin= 23
butPin = 17

duty = 75 #duty cycle btwn 0-100 on how bright it can be

#setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) #this is how you press a button

pwm = GPIO.PWM(pwmPin, 200) #200 is the frequency in Hz we want pwm to run at

GPIO.output(ledPin, GPIO.LOW)#sets blinking led to off initially 
pwm.start(duty)

try:
    while True:
        #if button not pressed (bright red)
        if GPIO.input(butPin):
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.LOW)
        else:               #if button pressed (blink green, bright <--> dim red)
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)

            pwm.ChangeDutyCycle(100 - duty)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.5)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
