import pigpio
import time

pin = 18
start_sleep_time = 2
freq = 300 # this is the lowest freq blinking is invisible to slo mo video
dc = .005 # range ~0.004-100 0 = off, 100 = fully on
dc = dc * 10000 # real range is 0 - 1000000

pi=pigpio.pi()
print("using GPIO pin %d"%pin)
print("resetting pwm dc to 0")
pi.hardware_PWM(pin,freq,0)
print("going to sleep for %d seconds"%start_sleep_time)
time.sleep(start_sleep_time)
print("starting pwm with freq[%d] and dc[%d]"%(freq,dc))
pi.hardware_PWM(pin,freq,dc)
