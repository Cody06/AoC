
inpList = []

with open('input.txt') as f:
	for line in f:
		inpList.append(line.strip('\n'))

bitWidth = len(inpList[0])

# Part 1
gamRateBit = []
epsRateBit = []

def zeroBitsFill(bitList, bitWidth):	# fill empty bits
	for i in range(bitWidth):
		bitList.append(0)

zeroBitsFill(gamRateBit, bitWidth)
zeroBitsFill(epsRateBit, bitWidth)
	
for i in range(bitWidth):	# go column by column
	zeros = 0
	ones = 0
	for bitStr in inpList:	# go through each bit
		if int(bitStr[i]) == 0:
			zeros += 1
		else:
			ones += 1
	gamRateBit[i] = 0 if zeros > ones else 1

for i in range(bitWidth):
	epsRateBit[i] = 0 if gamRateBit[i] == 1 else 1

def bitToDec(bitList, bitWidth):
	dec = 0
	rightToLeft = bitWidth - 1
	for i in range(bitWidth):
		dec += bitList[rightToLeft] * 2 ** (i)
		rightToLeft -= 1

	return dec

gamRateDec = bitToDec(gamRateBit, bitWidth)
epsRateDec = bitToDec(epsRateBit, bitWidth)

#print(f"Gam rate: {gamRateBin} -> {gamRateDec}")
#print(f"Eps Rate: {epsRateBin}  -> {epsRateDec}")
print(f"Power consumption: {gamRateDec * epsRateDec}")

# Part 2
oxygenBitStrList = []		# holds the bits that match criteria
co2BitStrList = []

rmOxygenBits = []		# holds the bits that need to be removed
rmCo2Bits = []

def strBitToDec(bitStr):
	bitList = []
	for bit in bitStr:
		bitList.append(int(bit))
	return bitToDec(bitList, len(bitList))

def most_common_bit(bitStrList, index):
	zeros = 0
	ones = 0
	for bitStr in bitStrList:
		if bitStr[index] == '0': 
			zeros += 1
		else:
			ones += 1

	return 1 if ones >= zeros else 0

for i in range(bitWidth):							# column by column (position by position)
	if i == 0:										# case for first bit
		for bitStr in inpList:						# row by row		
			if int(bitStr[0]) == gamRateBit[0]:		# Gamma rate contains the most common bits
				oxygenBitStrList.append(bitStr)
			else:									# looking for least common
				co2BitStrList.append(bitStr)
	else:											# case for all following bits (check which bit nums we remove)
		for bitStr in oxygenBitStrList:				# the initial oxygen bit nums	
			if int(bitStr[i]) != most_common_bit(oxygenBitStrList, i):
				rmOxygenBits.append(bitStr) 	# save in a list to remove not most common ones

		for bitStr in rmOxygenBits:
			if bitStr in oxygenBitStrList:
				if len(oxygenBitStrList) > 1:
					oxygenBitStrList.remove(bitStr)
				else:
					break

		for bitStr in co2BitStrList:
			if int(bitStr[i]) == most_common_bit(co2BitStrList, i):
				rmCo2Bits.append(bitStr)		# save in list to remove the most common ones

		for bitStr in rmCo2Bits:
			if bitStr in co2BitStrList:
				if len(co2BitStrList) > 1:
					co2BitStrList.remove(bitStr)
				else:
					break

oxygenDec = strBitToDec(oxygenBitStrList[0])
co2Dec = strBitToDec(co2BitStrList[0])

print(f"Oxygen: {oxygenBitStrList} -> {oxygenDec}")
print(f"CO2: {co2BitStrList} -> {co2Dec}")

print(f"Life support: {oxygenDec * co2Dec}")
