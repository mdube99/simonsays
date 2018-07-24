import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

colors = ['R', 'G', 'B', 'Y']
# this script appends a value to a list

def loop():
	while True:
		crand = random.randint(0,3)
		LED.setColor(colors[crand])
		time.sleep(0.5)
		LED.noColor()

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		LED.destroy()
		print "\n LED Turned off."

