import readGame


#######################################################
# These are some Helper functions which you have to use 
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_corner(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNextState(self, oldPos, direction):
#######################################################
class game:
	def __init__(self, filePath):
		self.gameState = readGame.readGameState(filePath)
		self.nodesExpanded = 0
		self.trace = []

		self.myDestinationState = [[0 for x in range(7)] for x in range(7)]
		for i in range(7):
			for j in range(7):
				if self.gameState[i][j] == -1:
					self.myDestinationState[i][j] = -1
				elif self.gameState[i][j] == 1:
					self.myDestinationState[i][j] = 0
				elif self.gameState[i][j] == 0:
					self.myDestinationState[i][j] = 0

		self.myDestinationState[3][3] = 1

	def is_corner(self, pos):
		########################################
		# You have to make changes from here
		# check for if the new positon is a corner or not
		# return true if the position is a corner

		#before checking gameState, must make sure index in boundary
		if pos[0] < 0 or pos[0] > 6 or pos[1] < 0 or pos[1] > 6:
			return True
		elif self.gameState[pos[0]][pos[1]] == -1:
			return True

		return False

	def getNextPosition(self, oldPos, direction):
		#########################################
		# YOU HAVE TO MAKE CHANGES HERE
		# See DIRECTION dictionary in config.py and add
		# this to oldPos to get new position of the peg if moved
		# in given direction , you can remove next line
		oldPos = (oldPos[0] + direction[0] * 2, oldPos[1] + direction[1] * 2)
		return oldPos

	def is_validMove(self, oldPos, direction):
		#########################################
		# DONT change Things in here
		# In this we have got the next peg position and
		# below lines check for if the new move is a corner
		newPos = self.getNextPosition(oldPos, direction)
		if self.is_corner(newPos):
			return False
		#########################################

		########################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# check for cases like:
		# if new move is already occupied
		# or new move is outside peg Board
		# Remove next line according to your convenience

		midPos = (oldPos[0] + direction[0], oldPos[1] + direction[1])

		# is_corner function has already checked if new move is outside peg board
		if self.gameState[midPos[0]][midPos[1]] != 1:
			return False
		elif self.gameState[newPos[0]][newPos[1]] == 1:
			return False
		return True

	def getNextState(self, oldPos, direction):
		###############################################
		# DONT Change Things in here
		self.nodesExpanded += 1
		if not self.is_validMove(oldPos, direction):
			print "Error, You are not checking for valid move"
			exit(0)
		###############################################

		###############################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# Update the gameState after moving peg
		# eg: remove crossed over pegs by replacing it's
		# position in gameState by 0
		# and updating new peg position as 1

		midPos = (oldPos[0] + direction[0], oldPos[1] + direction[1])
		newPos = self.getNextPosition(oldPos, direction)

		self.trace.append(oldPos)
		self.trace.append(newPos)

		self.gameState[oldPos[0]][oldPos[1]] = 0
		self.gameState[midPos[0]][midPos[1]] = 0
		self.gameState[newPos[0]][newPos[1]] = 1

		return self.gameState

	def reachDestination(self):
		for row in range(7):
			for col in range(7):
				if self.gameState[row][col] != self.myDestinationState[row][col]:
					return False
		return True

	def traceBack(self):
		traceLenth = len(self.trace)

		newPos = self.trace[traceLenth - 1]
		oldPos = self.trace[traceLenth - 2]
		midPos = ((newPos[0] + oldPos[0]) / 2, (newPos[1] + oldPos[1]) / 2)

		self.gameState[newPos[0]][newPos[1]] = 0
		self.gameState[midPos[0]][midPos[1]] = 1
		self.gameState[oldPos[0]][oldPos[1]] = 1

		lastPos = self.trace[traceLenth-1]
		self.trace.remove(lastPos)
		traceLenth = len(self.trace)
		lastPos = self.trace[traceLenth-1]
		self.trace.remove(lastPos)


		return oldPos
