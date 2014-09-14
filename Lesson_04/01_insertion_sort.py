#!/usr/bin/python3

def insertion_sort(array):

	for i in range(1, len(array)):
		k = i 
		while k > 0 and array[k] < array[k-1]:
			print(array)
			array[k], array[k-1] = array[k-1], array[k]
			k -= 1

	return array


def main():
	test = [12, 24, 6456, 13, 256, 1, 6, 786, 3543]

	# print(test)
	print("\n{}  <-- sorted".format(insertion_sort(test)))


main()