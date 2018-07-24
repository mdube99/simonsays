import time

# this script demonstrates how to  use try:except structure

count = 0

def loop():
	global count
	#Variable must be declared as global before being used in function
	while True:
		print "Hello World!"
		time.sleep(1)
		count += 1	
		if count == 5:
			print 'Printed 5 times'
			break

if  __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print ' Good bye'
