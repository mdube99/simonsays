import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
from getpass import getpass

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 1
buzz_pin = 32

#set passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequencies = [220, 440, 880, 1760]
colors = ['R', 'G', 'B', 'Y']
clist = []
freq_seq = []

# clist is definited as an empty list to append the colors into it from the 'colors' list
# this script appends a value to a list

def validate_guess(color_sequence_string, uinput):
	if color_sequence_string ==  uinput:
		print "Correct guess", color_sequence_string
		print uinput
	else:
		print "Your guess is incorrect", color_sequence_string
		LED.destroy()
		Buzz.stop()
		exit()

def loop():
	n = random.randint(0,3)
	clist.append(colors[n])
	freq_seq.append(frequencies[n])
	while True:
		for i in range(0, len(clist)):
			# for loop to get the range 0 then to the clist (list that gets appended with the colors)
			LED.setColor(clist[i])
			Buzz.ChangeFrequency(freq_seq[i])
			Buzz.start(50)
			time.sleep(0.5)
			Buzz.stop()
			LED.noColor()
			time.sleep(0.5)
		uinput = getpass ("What is the next color in the sequence?")
		color_sequence_string = ''.join(clist)
		validate_guess(color_sequence_string, uinput.upper())
		n = random.randint(0,3)
		clist.append(colors[n])
		freq_seq.append(frequencies[n])
		
def append_list():
	clist.append(clist[crand])
	color_string = ''.join(clist)

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		LED.destroy()
		Buzz.stop()
		print "\n LED Turned off."

