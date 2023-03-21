import os
class SingleFoodSearchProblem:
	def __init__(self, nameFile):
		self.maze=self.readMaze(nameFile)
		self.startState=self.getStartState()
		self.goalState=self.getGoalState()
		self.cost=0
		self.actions=['N','S','E','W','Stop']

	def readMaze(self,nameFile):
		maze=[]
		with open(nameFile) as f:
			for line in f:
				maze.append(list(line.strip()))
		return maze
	
	def getStartState(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				if self.maze[i][j]=='P':
					return (i,j)
		return None
	
	def getGoalState(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				if self.maze[i][j]=='.':
					return (i,j)
		return None
	
	def getSuccessors(self,state):
		successors=[]
		for action in self.actions:
			x,y=state
			if action=='N':
				x-=1
			elif action=='S':
				x+=1
			elif action=='E':
				y+=1
			elif action=='W':
				y-=1
			elif action=='Stop':
				pass
			if 0<=x<len(self.maze) and 0<=y<len(self.maze[1]) and self.maze[x][y]!='%':
				successors.append(((x,y),action,1))
		return successors
	
	def isValidMove(self,x, y):
		return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[1]) and self.maze[x][y] != '%'

	def isGoalState(self,state):
		return state == self.goalState
	
	def getCostOfActions(self,actions):
		return len(actions)
	
	def printMaze(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				print(self.maze[i][j],end='')
			print()

	def animate(self,actions):
		for action in actions:
			os.system('cls')
			x,y=self.startState
			self.maze[x][y] = ' '
			if action=='N':
				x-=1
			elif action=='S':
				x+=1
			elif action=='E':
				y+=1
			elif action=='W':
				y-=1
			elif action=='Stop':
				pass
			self.maze[x][y]='P'
			self.startState=(x,y)
			self.printMaze()
			self.maze[x][y]=' '
			input('Enter')


class MultiFoodSearchProblem:
	def __init__(self, nameFile):
		self.maze=self.readMaze(nameFile)
		self.startState=self.getStartState()
		self.goalState=self.getGoalState()
		self.cost=0
		self.actions=['N','S','E','W','Stop']

	def readMaze(self,nameFile):
		maze=[]
		with open(nameFile) as f:
			for line in f:
				maze.append(list(line.strip()))
		return maze
	
	def getStartState(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):#Fix len
				if self.maze[i][j]=='P':
					return (i,j)
		return None
	
	def getGoalState(self):
		__len=len(self.maze)
		food_list=[]
		for i in range(__len):
			for j in range(len(self.maze[i])):
				if self.maze[i][j]=='.':
					food_list.append((i,j))
		return food_list
	
	def getSuccessors(self,state):
		successors=[]
		for action in self.actions:
			x,y=state
			if action=='N':
				x-=1
			elif action=='S':
				x+=1
			elif action=='E':
				y+=1
			elif action=='W':
				y-=1
			elif action=='Stop':
				pass
			if 0<=x<len(self.maze) and 0<=y<len(self.maze[1]) and self.maze[x][y]!='%':
				successors.append(((x,y),action,1))
		return successors
	
	def isValidMove(self,x, y):
		return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[1]) and self.maze[x][y] != '%'

	def isGoalState(self,state):
		return state in self.goalState
	
	def getCostOfActions(self,actions):
		return len(actions)
	
	def printMaze(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				print(self.maze[i][j],end='')
			print()

	def animate(self,actions):
		for action in actions:
			os.system('cls')
			x,y=self.startState
			self.maze[x][y] = ' '
			if action=='N':
				x-=1
			elif action=='S':
				x+=1
			elif action=='E':
				y+=1
			elif action=='W':
				y-=1
			elif action=='Stop':
				pass
			self.maze[x][y]='P'
			self.startState=(x,y)
			self.printMaze()
			self.maze[x][y]=' '
			input('Enter')
		
	def getNumFood(self):
		return len(self.goalState)

	def getCostOfActions(self,actions):
		return len(actions)
	

class EightQueenProblem:
	def __init__(self,fileName):
		self.board=self.readBoard(fileName)

	def readBoard(self,fileName):
		board=[]
		with open(fileName) as f:
			for line in f:
				board.append(list(line.strip()))
		return board
	
	def printBoard(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				print(self.board[i][j],end='')
			print()

	def h(self, state):
		_size = len(state)
		queen_pairs = set()
		_h = 0
		
		for i, j in [(i, j) for i in range(_size) for j in range(_size) if state[i][j]]:
			for k in range(_size):
				if state[i][k] == 'Q' and k != j and (i, j, i, k) not in queen_pairs:
					_h += 1
					queen_pairs.add((i, j, i, k))

				if state[k][j] == 'Q' and k != i and (i, j, k, j) not in queen_pairs:
					_h += 1
					queen_pairs.add((i, j, k, j))

			for l, m in [(i - d, j + d) for d in range(1, _size) if 0 <= i - d < _size and 0 <= j + d < _size]:
				if state[l][m] == 'Q' and (i, j, l, m) not in queen_pairs:
					_h += 1
					queen_pairs.add((i, j, l, m))

			for l, m in [(i + d, j - d) for d in range(1, _size) if 0 <= i + d < _size and 0 <= j - d < _size]:
				if state[l][m] == 'Q' and (i, j, l, m) not in queen_pairs:
					_h += 1
					queen_pairs.add((i, j, l, m))

			for l, m in [(i - d, j - d) for d in range(1, _size) if 0 <= i - d < _size and 0 <= j - d < _size]:
				if state[l][m] == 'Q' and (i, j, l, m) not in queen_pairs:
					_h += 1
					queen_pairs.add((i, j, l, m))

			for l, m in [(i + d, j + d) for d in range(1, _size) if 0 <= i + d < _size and 0 <= j + d < _size]:
				if state[l][m] == 'Q' and (i, j, l, m) not in queen_pairs:
					_h += 1
					queen_pairs.add((i, j, l, m))
		
		return _h

	def hill_climbing_search(self):
		def deep_copy(state):
			_state=[]
			for i in range(len(state)):
				_state.append([])
				for j in range(len(state[i])):
					_state[i].append(state[i][j])
			return _state

		_size=len(self.board)
		_state=[]
		for i in range(_size):
			_state.append(['0']*_size)
		for i in range(_size):
			for j in range(_size):
				if self.board[i][j]=='Q':
					_state[i][j]='Q'
		_h=self.h(_state)
		while True:
			_h1=100000000
			_state1=[]
			for i in range(_size):
				for j in range(_size):
					if _state[i][j]=='Q':
						for k in range(_size):
							if k!=j:
								_state1=deep_copy(_state)
								_state1[i][j]='0'
								_state1[i][k]='Q'
								_h1=min(_h1,self.h(_state1))
			if _h1<_h:
				_h=_h1
				_state=_state1
			else:
				return _state