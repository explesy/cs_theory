#!/usr/bin/python3

from itertools import zip_longest

def arrays_combine(a, b):

	array = []

	# x - iterrator for a, y - for b
	x,y = 0, 0

	# print(len(a), len(b))

	while(x != len(a) or y != len(b)):
	
		if(a[x] < b[y]):
			array.append(a[x])
			x += 1
		elif(a[x] == b[y]):
			array.append(a[x])
			array.append(b[y])
			x += 1
			y += 1
		else:
			array.append(b[y])
			y += 1

		if(x == len(a)):
			array.append(b[y])
			y += 1
			continue
		if(y == len(b)):
			array.append(a[x])
			x += 1
			continue
		
		print(x, y, array)

	return array


def main():
	test_01 = [1, 6, 12, 13, 24, 256, 786, 3543, 6456]
	test_02 = [555, 777, 9999]

	print("\n{}  <-- combined".format(arrays_combine(test_01, test_02)))


main()