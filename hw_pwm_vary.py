import pigpio
import time

pin = 18
sleep_time = .00001
start_sleep_time = 5
freq = 300

pi=pigpio.pi()

pi.hardware_PWM(pin,freq,0)
#time.sleep(start_sleep_time)

while 1:
	for i in range(1,1000000):
		dc= i
		if i%1000 == 0:
			print(pin, freq, dc)
		pi.hardware_PWM(pin, freq, dc)
		time.sleep(sleep_time)
	print("peak")
	for i in range(1, 1000000):
		dc= (999999-i)
		if i%1000 == 0:
			print(pin, freq, dc)
		pi.hardware_PWM(pin, freq, dc)
		time.sleep(sleep_time)
	time.sleep(5)


