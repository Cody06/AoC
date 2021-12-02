destination = {'horizontal': 0, 'depth': 0}

with open('d2_input.txt') as f:
	for line in f:
		lineTuple = line.partition(' ')  # ('down', ' ', '5')
		move = lineTuple[0]
		units = int(lineTuple[2])
		
		if move == "forward":
			destination['horizontal'] += units
		elif move == "down":
			destination['depth'] += units
		else:	# moving up
			destination['depth'] -= units

	#print(destination['horizontal'] * destination['depth'])


destination2 = {'horizontal': 0, 'depth': 0, 'aim': 0}

with open('d2_input.txt') as f:
	for line in f:
		lineTuple = line.partition(' ')
		move = lineTuple[0]
		units = int(lineTuple[2])

		if move == "forward":
			destination2['horizontal'] += units
			destination2['depth'] += destination2['aim'] * units
		elif move == "down":
			destination2['aim'] += units
		else: # aiming up
			destination2['aim'] -= units

	#print(destination2['horizontal'] * destination2['depth'])


# _____ Same as above, but wrapped in functions _____
def dive(cmdsList: 'List[{cmd: units}]') -> int:
	'''
		Based on the command in the list, calculate the final destination:
			- forward: increase horizontal based on units
			- down: increase depth based on units
			- up: decrease depth based on units
		input: a list of dictionaries
		output: an integer (horizontal * depth)
	'''
	destination = {'horizontal': 0, 'depth': 0}

	for cmdDict in cmdsList:					# iterate through the commands
		for cmd, units in cmdDict.items():		# get the key and value from a dict of length 1
			if cmd == "forward":
				destination['horizontal'] += units
			elif cmd == "down":
				destination['depth'] += units
			else:
				destination['depth'] -= units
	
	return destination['horizontal'] * destination['depth']


def dive_aim(cmdsList: 'List[{cmd: units}]') -> int:
	'''
		Similar as above, except:
			- forward: increase horizontal by X and increase depth by aim * X
			- down: increase aim
			- up: decrease aim
		input: a list of dictionaries
		output: an integer (horizontal * depth)
	'''
	destination = {'horizontal': 0, 'depth': 0, 'aim': 0}

	for cmdDict in cmdsList:
		for cmd, units in cmdDict.items():
			if cmd == "forward":
				destination['horizontal'] += units
				destination['depth'] += destination['aim'] * units
			elif cmd == "down":
				destination['aim'] += units
			else: # aim up
				destination['aim'] -= units

	return destination['horizontal'] * destination['depth']


if __name__ == "__main__":
	commandsList = []

	with open('d2_input.txt') as f:
		for line in f:
			lineTuple = line.partition(' ')   # ('down', ' ', '5')
			cmd = lineTuple[0]
			units = int(lineTuple[2])

			commandsList.append({cmd: units})

	print(f"Answer 1: {dive(commandsList)}")
	print(f"Answer 2: {dive_aim(commandsList)}")

