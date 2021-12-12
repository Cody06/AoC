# Each board is an object containing columns and rows
# If a column or row contains all true (return the keys)
def print_board(boardObj):
	for row in boardObj.numsGrid:
		print(row)

class Board:
	def __init__(self, numsGrid, draw=None):
		self.numsGrid = numsGrid

		self.gridWidth = len(numsGrid[0])
		# Track when one row or coumn gets completed
		# index corresponds to the given row or column. when one is 5, the board won
		
		self.rowsCompleted = []
		self.colsCompleted = []	
		for i in range(self.gridWidth):
			self.rowsCompleted.append(0)
			self.colsCompleted.append(0)

		self.winner = False

	def hasWon(self, draw):
		for row in range(self.gridWidth):
			for col in range(self.gridWidth):
				if draw == self.numsGrid[row][col]:
					self.rowsCompleted[row] += 1
					self.colsCompleted[col] += 1
					self.numsGrid[row][col] = '*'

				if self.gridWidth in self.rowsCompleted or self.gridWidth in self.colsCompleted:
					# calculate all the remaining numbers in the board
					points = 0
					for rows in self.numsGrid:
						for num in rows:
							if num != '*':
								points += num

					print(f"---WINNER {points * draw}")
					self.winner = True
					return True



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
print(f"draws = {draws}")
print()

# Get all the boards (create the grids)
# Store each board in a list:
grid = []		 # [[1, 2, 3], [4, 5, 6]]
boardsList = []  # [board1, board2, board3, ...]
counter = 1
numOfRows = 5

for rowStr in rowsStrList:
	if counter == numOfRows:  # we're at the last row of numbers
		grid.append(list(map(int, rowStr.split()))) # convert a string of numbers into a list of integers
		boardsList.append(Board(grid))
		counter = 1		# reset counter
		grid = []		# reset board
	else:
		grid.append(list(map(int, rowStr.split()))) 
		counter += 1



def findWinningBoard(draws, boardsList):
	for draw in draws:			# Pass a number and see if it's in in the given board
		for board in boardsList: 
			if board.hasWon(draw):
				print("Found best board")
				return
	

def worstBoard(draws, boardsList):
	for draw in draws:
		print(f"------------------------- draw: {draw}")
		for board in boardsList:
			if not board.winner:
				if board.hasWon(draw):
					print_board(board)
					print("___")
					

#findWinningBoard(draws,boardsList)
worstBoard(draws, boardsList)
