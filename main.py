from analysis import *

class Minesweeper:
	def __init__(self, n, bombs):
		self.n_board = n
		self.real_board = []
		self.player_board = []
		self.gen_real_board(bombs)
		self.gen_player_board()
		# self.analysis = Analysis('main.clp')

	def gen_real_board(self, bombs):
		for i in range(self.n_board):
			temp = []
			for j in range(self.n_board):
				temp.append(0)
			self.real_board.append(temp)
		self.reformat_board(bombs)
	
	def gen_player_board(self):
		for i in range(self.n_board):
			temp = []
			for j in range(self.n_board):
				temp.append('?')
			self.player_board.append(temp)

	def reformat_board(self, bombs):
		for bomb in bombs:
			self.real_board[int(bomb[0])][int(bomb[1])] = -1
			# self.analysis.create_facts(int(bomb[0]),int(bomb[1]),-1)
		self.recalc_board()

	def recalc_board(self):
		for i in range(self.n_board):
			for j in range(self.n_board):
				if(self.real_board[i][j]!=-1):
					self.real_board[i][j] = self.count_bombs(i,j)
					# self.analysis.create_facts(i,j,self.real_board[i][j])

	def count_bombs(self, i, j):
		res = 0
		n = self.n_board-1
		if(i>0):
			res += (self.real_board[i-1][j] == -1)
		if(i>0 and j>0):
			res += (self.real_board[i-1][j-1] == -1)
		if(i<n):
			res += (self.real_board[i+1][j] == -1)
		if(i<n and j<n):
			res += (self.real_board[i+1][j+1] == -1)
		if(j>0):
			res += (self.real_board[i][j-1] == -1)
		if(i<n and j>0):
			res += (self.real_board[i+1][j-1] == -1)
		if(j<n):
			res += (self.real_board[i][j+1] == -1)
		if(i>0 and j<n):
			res += (self.real_board[i-1][j+1] == -1)
		return res

	def check_win(self):
		for i in range(len(self.player_board)):
			for j in range(len(self.player_board)):
				if(self.player_board[i][j]=='?'):
					return False
		return True

	def validate(self, move):
		m = move.split(" ")
		arg = len(m)
		if(arg==2):
			if(m[0] != 'f'):
				return False
			return (len(m[1].split(','))==2)
		elif(arg==1):
			return (len(m[0].split(','))==2)
		else:
			return False

	def process_move(self, move):
		mov = move.split(" ")
		if(len(mov)==2):
			m = mov[1].split(",")
			i = int(m[0])
			j = int(m[1])
			if(self.player_board[i][j] == 'f'):
				self.player_board[i][j] = '?'
			else:
				self.player_board[i][j] = 'f'
		else:
			m = mov[0].split(",")
			i = int(m[0])
			j = int(m[1])
			self.reveal_board(i,j)

	def choose_cell(self, i, j):
		self.player_board[i][j] = self.real_board[i][j]
	
	def reveal_board(self,i,j):
		n = self.n_board-1
		if(self.real_board[i][j]!=0):
			if(self.real_board[i][j]!=-1 and self.player_board[i][j]=='?'):
					self.player_board[i][j] = self.real_board[i][j]
			return 
		else:
			if(self.real_board[i][j] == 0):
				self.player_board[i][j] = self.real_board[i][j]
				if(i>0):
					if(self.real_board[i-1][j]!=-1 and self.player_board[i-1][j]=='?'):
						self.player_board[i-1][j] = self.real_board[i-1][j]
						self.reveal_board(i-1,j)
				if(i>0 and j>0):
					if(self.real_board[i-1][j-1]!=-1 and self.player_board[i-1][j-1]=='?'):
						self.player_board[i-1][j-1] = self.real_board[i-1][j-1]
						self.reveal_board(i-1,j-1)
				if(i<n):
					if(self.real_board[i+1][j]!=-1 and self.player_board[i+1][j]=='?'):
						self.player_board[i+1][j] = self.real_board[i+1][j]
						self.reveal_board(i+1,j)
				if(i<n and j<n):
					if(self.real_board[i+1][j+1]!=-1 and self.player_board[i+1][j+1]=='?'):
						self.player_board[i+1][j+1] = self.real_board[i+1][j+1]
						self.reveal_board(i+1,j+1)
				if(j>0):
					if(self.real_board[i][j-1]!=-1 and self.player_board[i][j-1]=='?'):
						self.player_board[i][j-1] = self.real_board[i][j-1]
						self.reveal_board(i,j-1)
				if(i<n and j>0):
					if(self.real_board[i+1][j-1]!=-1 and self.player_board[i+1][j-1]=='?'):
						self.player_board[i+1][j-1] = self.real_board[i+1][j-1]
						self.reveal_board(i+1,j-1)
				if(j<n):
					if(self.real_board[i][j+1]!=-1 and self.player_board[i][j+1]=='?'):
						self.player_board[i][j+1] = self.real_board[i][j+1]
						self.reveal_board(i,j+1)
				if(i>0 and j<n):
					if(self.real_board[i-1][j+1]!=-1 and self.player_board[i-1][j+1]=='?'):
						self.player_board[i-1][j+1] = self.real_board[i-1][j+1]
						self.reveal_board(i-1,j+1)

	def isBomb(self,i,j):
		return (self.real_board[i][j] == -1)

	def print_real_board(self):
		for i in range(len(self.real_board)):
			temp = ""
			for j in range(len(self.real_board)):
				temp += ('b' if(self.real_board[i][j] == -1) else str(self.real_board[i][j])) + " "
			print(temp)

	def print_player_board(self):
		for i in range(len(self.player_board)):
			temp = ""
			for j in range(len(self.player_board)):
				temp += str(self.player_board[i][j]) + " "
			print(temp)

	def generate_facts(self, i, j):
		facts = []
		n = self.n_board-1
		if(i>0):
			facts.append(['up',i,j,self.real_board[i-1][j]])
		if(i>0 and j>0):
			facts.append(['up-left',i,j,self.real_board[i-1][j-1]])
		if(i<n):
			facts.append(['down',i,j,self.real_board[i+1][j]])
		if(i<n and j<n):
			facts.append(['down-right',i,j,self.real_board[i+1][j+1]])
		if(j>0):
			facts.append(['left',i,j,self.real_board[i][j-1]])
		if(i<n and j>0):
			facts.append(['down-left',i,j,self.real_board[i+1][j-1]])
		if(j<n):
			facts.append(['right',i,j,self.real_board[i][j+1]])
		if(i>0 and j<n):
			facts.append(['up-right',i,j,self.real_board[i-1][j+1]])
		return facts

# Main Program
n_board = int(input("Masukkan ukuran board: "))
while(n_board<4 or n_board>10):
	print("Board size must be between 4 and 10!")
	n_board = int(input("Masukkan ukuran board: "))

n_bomb = int(input("Masukkan jumlah bomb: "))
bombs = []

for i in range(n_bomb):
	bomb = input("Masukkan koordinat bomb : ").split(',')
	bombs.append(bomb)

minesweeper = Minesweeper(n_board,bombs)
# analysis = Analysis('main.clp')

print("Real Board:\n")
minesweeper.print_real_board()

# facts = minesweeper.generate_facts(0,0)
# analysis.assertFacts(facts)

# analysis.run()
# facts = analysis.matched_facts()

while(1):
	if(minesweeper.check_win()):
		print("You win!")
		break
	print("Player Board:\n")
	minesweeper.print_player_board()
	move= input("Your move (example : '1,3' to open or 'f 1,3' to flag) : ")
	if(minesweeper.validate(move)):
		mov = move.split(" ")
		if(len(mov)==1):
			m = mov[0].split(",")
			if(minesweeper.isBomb(int(m[0]),int(m[1]))):
				print("BOOM!!!")
				break
		minesweeper.process_move(move)
	else:
		print("Invalid move format!")