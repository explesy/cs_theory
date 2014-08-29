#!/usr/bin/python3

def hex_to_dec(y, numeral):
	''' Return decimal represntation of the digit in given numeral system '''

	dec = 0 
	power = len(y) - 1

	for digit in y:
		if digit.isdigit():
			dec += int(digit) * (numeral ** power)
		else:
			dec += int(chr_to_num(digit)) * (numeral ** power)

		power -= 1

	return dec

def dec_to_sept(x, numeral):
	''' Return represntation of decimal number in given number system '''
	res = ""
	while x:
		res += str(x%numeral)
		x //= numeral
	return res[::-1]


def is_hex_number(number):
	""" Check is our input is a hexadecimal number """
	import re
	pattern = re.compile('[0-7A-F]+')
	match = pattern.match(number)
	if match:
		return True
	else:
		return False

def chr_to_num(x):
  x = ord(x)
  if ord("0") <= x <= ord("9"): return x - ord("0")
  elif ord("a") <= x <= ord("z"): return x - ord("a") + 10
  else: return x - ord("A") + 10


def main():

	test = ["AB", "10", "115", "19F", "A", "BB", "1533C", "24AA"]
	numeral_from = 16
	numeral_to = 7
	for i in test:
		if(is_hex_number(i)):
			print("[V]", i, hex_to_dec(i, numeral_from), dec_to_sept(hex_to_dec(i, numeral_from), numeral_to))

		else:
			print("[ ]", i)

	# number = 0

	# print("""\n
	# 		**********************\n
	# 		* Input quit to exit *\n
	# 		**********************\n
	# 		""")

	# while(number != "quit"):
	# 	number = input("Please input octal number: ")
	# 	if(is_oct_number(number)):
	# 		# print("We have a number")
	# 		print("{} oct ---> {} dec".format(number, oct_to_dec(number)))
	# 	else:
	# 		print("It's don't looks like a octal number")


main()