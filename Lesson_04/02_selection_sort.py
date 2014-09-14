#!/usr/bin/python3

def selection_sort(array):

	for i in range(0, len(array)):
		min = i
		for k in range(i, len(array)):
			if array[k] < array[min]:
				min = k
		print(array)
		min_elt = array.pop(min)
		array.insert(i, min_elt)

	return array


def main():
	test = [12, 24, 6456, 13, 256, 1, 6, 786, 3543]

	# print(test)
	print("\n{}  <-- sorted".format(selection_sort(test)))


main()