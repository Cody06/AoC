
listOfdepths = []

with open('d1q1_input.txt') as f:	# questions 2 uses same input as question 1
	for line in f:
		listOfdepths.append(int(line.strip('\n')))


windowSums = []

for i in range(2, len(listOfdepths)):
	windowSums.append(listOfdepths[i - 2] + listOfdepths[i - 1] + listOfdepths[i])


numOfIncreases = 0

for i in range(1, len(windowSums)):
	if windowSums[i - 1] < windowSums[i]:
		numOfIncreases += 1

print(f"Number of increases: {numOfIncreases}")