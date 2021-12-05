# Each board is an object containing columns and rows
# If a column or row contains all true (return the keys)
class Board:
	def __init__(self, rowsList):
		self.rowsList = rowsList

# Get all the drawn numbers
draws = []
rowsStrList = []	# every row of numbers is stored as a string element

f = open('input.txt', 'r')
firstLine = f.readline().strip('\n')	# get the first line
drawsStrList = firstLine.split(',')			# split line in a list of strings ['1', '2', '3', ...]
# Store draws in a list of integers
for drawStr in drawsStrList:			
	draws.append(int(drawStr))			# draws = [1, 2, 3, ...]
next(f)									# go to the next line (where boards start)

for line in f:
	if line != '\n':	
		rowsStrList.append(line.strip('\n'))  # rowsStrList = [' 1 2 3', ' 4 5 6', ' 7 8 9', ...]

f.close()

# Get all the boards
# Store each board in a list: 
board = []		 # [[1, 2, 3], [4, 5, 6]]
boardsList = []  # [board1, board2, board3, ...]
counter = 1

for rowStr in rowsStrList:
	if counter == 5:  # we're at the last row of numbers
		board.append(list(map(int, rowStr.split()))) # convert a string of numbers into a list of integers
		boardsList.append(board)
		counter = 1		# reset counter
		board = []		# reset board
	else:
		board.append(list(map(int, rowStr.split()))) 
		counter += 1	 																	

print(f"boardsList = {boardsList}\n")

for board in boardsList:
	print(f"board = {board}")
	for row in board:
		print(f"row = {row}")