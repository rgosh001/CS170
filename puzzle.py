
#!/usr/bin/python
import os, sys, copy
clear = lambda: os.system('clear')

goal_state = [['1', '2', '3'], 
				['4', '5', '6'], 
				['7', '8', ' ']]


def initMenu():
	default = [['1', '2', '3'], 
				['4', ' ', '5'], 
				['6', '7', '8']]
	print "8-Puzzle Game Developed by Rashid!"
	print "First choose \"default\" or \"create your own\" puzzle: \n"
	print "1. Default Puzzle: "
	printPuzzle(default)
	print "\n2. Create your own\n"
	
	while(1):
		choice = raw_input("Choice: ")
		if(choice == '1'):
			return default
		elif(choice == '2'):
			return ownPuzzle()
	
	
def ownPuzzle():
	print "Please create your own puzzle and use a 0 for a blank spot:\n"
	
	blankUsed = 0
	
	firstrow = raw_input("Please enter the first row. Use spaces between numbers: ")
	firstrow = firstrow.split(' ')
	if('0' in firstrow):
		firstrow[firstrow.index('0')] = ' '
		blankUsed = 1
		
	while(1):
		secondrow = raw_input("Please enter the second row. Use spaces between numbers: ")
		secondrow = secondrow.split(' ')
		if(secondrow.find('0')):
			if(blankUsed != 0):
				print "Error: Blank space already used, please try again."
			elif(blankUsed):
				secondrow[secondrow.index('0')] = ' '
				blankUsed = 1
				break
	
	while(1):
		thirdrow = raw_input("Please enter the third row. Use spaces between numbers: ")
		thirdrow = thirdrow.split(' ')
		if(thirdrow.find('0')):
			if(blankUsed != 0):
				print "Error: Blank space already used, please try again."
			elif(blankUsed):
				thirdrow[thirdrow.index('0')] = ' '
				blankUsed = 1
				break
			
	puzzle = []
	puzzle.append(firstrow)
	puzzle.append(secondrow)
	puzzle.append(thirdrow)
	
	return puzzle

		
		

def algorithmChoice():
	print "Please choose an algorithms to use:"
	print "1. Uniform Cost Search"
	print "2. A*, misplaced tile heuristic"
	print "3: A*, Manhattan distance heuristic\n"

	while(1):
		choice = raw_input("Choice: ")
		if(choice == '1'):
			return "ucostSearch"
		elif(choice == '2'):
			return "mtileHeuristic"
		elif(choice == '3'):
			return "manhattan"
		else:
#			clear = lambda: os.system('clear')
			clear()
			print "Error: Entry invalid, please try again."
			print "Please choose an algorithms to use:"
			print "1. Uniform Cost Search"
			print "2. A*, misplaced tile heuristic"
			print "3: A*, Manhattan distance heuristic\n"
		return choice
		
def printPuzzle(array):
	print array[0]
	print array[1]
	print array[2]
	
	
class node:
	def __init__(self):
		self.depth = 0
		self.heuristic = 0
	def setPuzzle(self, puzzle):
		self.puzzleState = puzzle
	def printNode(self):
		print self.puzzleState[0][0] + " " + self.puzzleState[0][1] + " " + self.puzzleState[0][2]
		print self.puzzleState[1][0] + " " + self.puzzleState[1][1] + " " + self.puzzleState[1][2]
		print self.puzzleState[2][0] + " " + self.puzzleState[2][1] + " " + self.puzzleState[2][2]
		
		
def copyNodes(puzzle):
	newNode = copy.deepcopy(puzzle)
	return newNode
	
def expandNodes(puzzle):
	newNodes = []
	
	directionUP = copyNodes(puzzle)
	for x in puzzle:
		blankIndex = 0
		if(x.count(' ') == 1):
			if(x != puzzle[0]):
				blankIndex = x.index(' ')
				if(x == puzzle[1]):
					directionUP[1][blankIndex] = directionUP[0][blankIndex]
					directionUP[0][blankIndex] = ' '
					newNodes.append(directionUP)
				else:
					directionUP[2][blankIndex] = directionUP[1][blankIndex]
					directionUP[1][blankIndex] = ' '
					newNodes.append(directionUP)

	directionDown = copyNodes(puzzle)
	for x in puzzle:
		blankIndex = 0
		if(x.count(' ') == 1):
			if(x != puzzle[2]):
				blankIndex = x.index(' ')
				if(x == puzzle[0]):
					directionDown[0][blankIndex] = directionDown[1][blankIndex]
					directionDown[1][blankIndex] = ' '
					newNodes.append(directionDown)
				else:
					directionDown[1][blankIndex] = directionDown[2][blankIndex]
					directionDown[2][blankIndex] = ' '
					newNodes.append(directionDown)
					
	directionLeft = copyNodes(puzzle)
	for x in directionLeft:
		blankIndex = x.index(' ')
		if(x.count(' ') == 1):
			if(blankIndex != 0):
				x[blankIndex] = x[blankIndex - 1]
				x[blankIndex - 1] = ' '	
				newNodes.append(directionLeft)
	
	directionRight = copyNodes(puzzle)
	for x in directionRight:
		blankIndex = x.index(' ')
		if(x.count(' ') == 1):
			if(blankIndex != 2):
				x[blankIndex] = x[blankIndex + 1]
				x[blankIndex + 1] = ' '	
				newNodes.append(directionRight)
				
	return newNodes
	

def bubblesortAlg(puzzleList):
	#first element to be length - 1, 
	#the last element to 0, 
	#and we dequeue by -1.
	for x in xrange(len(queue)-1, 0, -1)

	
def search(puzzle, choice):
	expandedNodes = 0
	queueSize = 0
	queue = []
	
	puzzleList = node()
	puzzleList.setPuzzle(puzzle)
	puzzleList.depth = 0
	
	if(choice == "ucostSearch"):
		puzzleList.heuristic = 1
	if(choice == "mtileHeuristic"):
		return
	if(choice == "manhattan"):
		return
		
	queue.append(puzzleList)
	
	print queue[0].puzzleState
	
	while 1:
		if(len(queue) == 0):
			print "puzzle search done"
			sys.exit(0)
		
		frontNode = node()
		frontNode.puzzleState = queue[0].puzzleState
		frontNode.depth = queue[0].heuristic
		frontNode.heuristic = queue[0].depth
		
		print "The best state to expand with a g(n) = ", frontNode.depth, " and h(n) = ", frontNode.heuristic, "is... "
		print frontNode.printNode()
		print "Expanding this node..."
		
		queue.pop(0)
		
#		if(frontNode == goal_state):
#			print "goal"
#		else:
#			print "nope"
		
		allMovesPossible = expandNodes(frontNode.puzzleState)
		
		for x in expandedNodes:
			nodeToCheck = node()
			nodeToCheck.setPuzzle(x)
			if(choice == "ucostSearch"):
				nodeToCheck.heuristic = 1
			if(choice == "mtileHeuristic"):
				return
			if(choice == "manhattan"):
				return
				
			nodeToCheck.depth = puzzleList.depth + 1
			queue.append(nodeToCheck)
			expandedNodes = expandedNodes + 1
			
			if(len(queue) > queueSize):
				queueSize = len(queue)
		
		queue = bubblesort(queue)
			
			
		
		
		sys.exit(0)
	
	
	
		
	
	
	
	
	
	
	
	
	
	


if __name__ == "__main__":
	clear()
	choice = algorithmChoice()
	clear()
	print "User choice: " + choice
	puzzle = initMenu()
	clear()
	
	print "Puzzle is set to: \n"
	printPuzzle(puzzle)
	
	print "Starting Search...\n"
	search(puzzle, choice)