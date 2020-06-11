import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode (IO.BCM)

IO.setup(24,IO.OUT)
freq= 10000
sleep_time=1
duty_cycle=99

p = IO.PWM(24,freq)

p.start(duty_cycle)
while 1:
	time.sleep(1)

#while 1:
#    for x in range (99):
#        p.ChangeDutyCycle(x)
#        time.sleep(sleep_time)
#
#    for x in range (99):
#        p.ChangeDutyCycle(99-x)
#        time.sleep(sleep_time)
#    break
	
	
