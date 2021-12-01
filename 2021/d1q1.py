def open_file_get_integers_list(path_to_file):
	''' 
	Open file, read contents line by line, store as a list of integers and close automatically (without calling f.close())
	Return: list of integers
	'''
	listOfInts = []
	with open(path_to_file) as f:
		for line in f:
			listOfInts.append(int(line.strip('\n')))	# remove new-line and cast as integer

	return listOfInts


def count_increases(listOfInts):
	counter = 0
	for i in range(1, len(listOfInts)):
		if listOfInts[i - 1] < listOfInts[i]:
			counter += 1

	return counter


depths = open_file_get_integers_list('d1q1_input.txt')

numOfIncreases = count_increases(depths)

print(f"Number of increases: {numOfIncreases}")

