gameBoard = [
	'-', '-', '-',
	'-', '-', '-',
	'-', '-', '-',
]

comp = 'x'
human = 'o'

class Node:
	def __init__(self, state):
		self.state = state
		self.leafs = []
		self.value = 2

	def addLeafs(self, state):
		self.leafs.append(Node(state))

	def getLeafs(self):
		return self.leafs

	def getState(self):
		return self.state


#Verifica se houve vencedor
def winner(n):
	#Linha
	board = n.state
	player = board[0]
	if( ((board[0] == player) and (board[1] == player) and (board[2] == player)) or ((board[3] == player) and (board[4] == player) and (board[5] == player)) or ((board[6] == player) and (board[7] == player) and (board[8] == player))):
		if player == 'x':
			return 1
		else:
			return -1

	#Coluna
	if( ((board[0] == player) and (board[3] == player) and (board[6] == player)) or ((board[1] == player) and (board[4] == player) and (board[7] == player)) or ((board[2] == player) and (board[5] == player) and (board[8] == player))):
		if player == 'x':
			return 1
		else:
			return -1

	#Diagonal
	if( ((board[0] == player) and (board[4] == player) and (board[8] == player)) or ((board[2] == player) and (board[4] == player) and (board[6] == player)) ):
		if player == 'x':
			return 1
		else:
			return -1
	
	return 0

#Inicializa a arvore
def initTree(board):
	return Node(board)

#A cada nó, calcula os seus filhos
def addSublevel(board, n, player):
	copyBoard = board.copy()
	for i in range(9):
		if copyBoard[i] == '-':
			copyBoard[i] = player
			n.addLeafs(copyBoard)
			copyBoard = board.copy()

#Preenche toda a árvore
def fillTree(n):
	for depth_0 in n.getLeafs():
		aux_0 = depth_0
		addSublevel(aux_0.state, aux_0, human)
		for depth_1 in depth_0.getLeafs():
			aux_1 = depth_1
			addSublevel(aux_1.state, aux_1, comp)
			for depth_2 in depth_1.getLeafs():
				aux_2 = depth_2
				addSublevel(aux_2.state, aux_2, human)
				for depth_3 in depth_2.getLeafs():
					aux_3 = depth_3
					addSublevel(aux_3.state, aux_3, comp)
					for depth_4 in depth_3.getLeafs():
						aux_4 = depth_4
						addSublevel(aux_4.state, aux_4, human)
						value = winner(aux_4)
						if value:
							aux_4.value = value
						for depth_5 in depth_4.getLeafs():
							aux_5 = depth_5
							addSublevel(aux_5.state, aux_5, comp)
							value = winner(aux_5)
							if value:
								aux_5.value = value
							for depth_6 in depth_5.getLeafs():
								aux_6 = depth_6
								addSublevel(aux_6.state, aux_6, human)
								value = winner(aux_6)
								if value:
									aux_6.value = value
								for depth_7 in depth_6.getLeafs():
									aux_7 = depth_7
									addSublevel(aux_7.state, aux_7, comp)
									aux_7.value = winner(aux_7)
	return n

def printBoard(board):
	print('{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n'.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))

def minimax(n, depth):
	_min = 2
	_max = 2

	if depth == 1:
		n.value = winner(n.getLeafs()[0])
		return

	for i in range(depth):
		if n.getLeafs()[i].value == 2:
			minimax(n.getLeafs()[i], depth-1)

	#MAX -> COMPUTER
	if depth % 2 == 0:
		for i in range(depth):
			if _max == 2:
				_max = n.getLeafs()[i].value
			elif n.getLeafs()[i].value == 1:
				_max = 1
				break
			elif n.getLeafs()[i].value > _max:
				_max = n.getLeafs()[i].value

		n.value = _max

	#MIN -> HUMAN
	else:
		for i in range(depth):
			if _min == 2:
				_min = n.getLeafs()[i].value
			elif n.getLeafs()[i].value == -1:
				_min = -1
				break
			elif n.getLeafs()[i].value < _min:
				_min = n.getLeafs()[i].value

		n.value = _min

	return

def printResult(n, depth):
	level = 10 - depth
	if depth == 1:
		if n.value != 2:
			print('depth: {} value: {}'.format(level, n.value))
			printBoard(n.state)
			return

	for i in range(depth):
		printResult(n.getLeafs()[i], depth-1)

	if n.value != 2:
		print('depth: {} value: {}'.format(level, n.value))
		printBoard(n.state)

def main():
	n = initTree(gameBoard)
	addSublevel(gameBoard, n, comp)
	n = fillTree(n)
	minimax(n,9)
	printResult(n,9)
	#print('Raiz: {}'.format(n.value))


main()