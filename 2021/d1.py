def sonar_sweep(depths: 'List[int]') -> int:
	'''
		In a list of integers, compute the number of times the following number is larger than the previous
		input: a list of integers
		output: an integer
	'''
	count = 0
	for i in range(1, len(depths)):
		if depths[i - 1] < depths[i]:		# increase if d(109) < d(200)
			count += 1

	return count


def sonar_sweep_window(depths: 'List[int]') -> int:
	'''
		In a list of integers, first compute a moving window of the sum of three consecutive integers.
		Then use the previous function to return the number of increases between the following window sum and the previous.
		input: list of integers
		output: an integer
	'''
	threeDepthsSums = []			# list of the sum of three consecutive depths 
	for i in range(2, len(depths)):
		threeDepthsSums.append(depths[i - 2] + depths[i - 1] + depths[i])

	return sonar_sweep(threeDepthsSums)		# previous question is a helper function

if __name__ == '__main__':
	depths = []

	with open('d1_input.txt') as f:					# open file in read mode and automatically close it (no need for f.close())
		for line in f:								# iterate line by line
			depths.append(int(line.strip('\n')))	# store each formatted depth in the depths list

	print(f"Answer 1: {sonar_sweep(depths)}")
	print(f"Answer 2: {sonar_sweep_window(depths)}")

