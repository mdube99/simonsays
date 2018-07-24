from getpass import getpass
#getpass keeps it from showing what you're typing (as if it's a password)

# This script shows how to get user input

print "What is your name?"
name = raw_input()

color = getpass('What is your favorite color? ')

print "Hi, ", name
print "Your favorite color is: ", color
