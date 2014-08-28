#!/usr/bin/python3

def oct_to_dec(oct):
	''' Return decimal represntation of given octal number '''

	dec = 0 
	power = len(oct) - 1

	for digit in oct:
		dec += int(digit) * (8 ** power)
		power -= 1

	return dec

def is_oct_number(number):
	""" Check is our input is a ocatal number """
	import re
	pattern = re.compile('[0-7]+$')
	match = pattern.match(number)
	if match:
		return True
	else:
		return False


def main():

	number = 0

	print("""\n
			**********************\n
			* Input quit to exit *\n
			**********************\n
			""")

	while(number != "quit"):
		number = input("Please input octal number: ")
		if(is_oct_number(number)):
			# print("We have a number")
			print("{} oct ---> {} dec".format(number, oct_to_dec(number)))
		else:
			print("It's don't looks like a octal number")


main()