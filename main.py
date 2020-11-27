def print_real_board(board):
	for i in range(len(board)):
		temp = ""
		for j in range(len(board)):
			temp += ('b' if(board[i][j] == -1) else str(board[i][j])) + " "
		print(temp)

def print_player_board(board):
	for i in range(len(board)):
		temp = ""
		for j in range(len(board)):
			temp += str(board[i][j]) + " "
		print(temp)

def gen_board(n):
	res = []
	for i in range(n):
		temp = []
		for j in range(n):
			temp.append(0)
		res.append(temp)
	return res

def gen_player_board(n):
	res = []
	for i in range(n):
		temp = []
		for j in range(n):
			temp.append('?')
		res.append(temp)
	return res

def reformat_board(board,bombs):
	for bomb in bombs:
		board[int(bomb[0])][int(bomb[1])] = -1
	recalc_board(board)

def recalc_board(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if(board[i][j]!=-1):
				board[i][j] = count_bombs(board,i,j)

def count_bombs(board,i,j):
	res = 0
	n = len(board)-1
	if(i>0):
		res += (board[i-1][j] == -1)
	if(i>0 and j>0):
		res += (board[i-1][j-1] == -1)
	if(i<n):
		res += (board[i+1][j] == -1)
	if(i<n and j<n):
		res += (board[i+1][j+1] == -1)
	if(j>0):
		res += (board[i][j-1] == -1)
	if(i<n and j>0):
		res += (board[i+1][j-1] == -1)
	if(j<n):
		res += (board[i][j+1] == -1)
	if(i>0 and j<n):
		res += (board[i-1][j+1] == -1)
	return res

def check_win(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if(board[i][j]=='?'):
				return False
	return True

def validate(move):
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

def process_move(r_board,p_board,move):
	mov = move.split(" ")
	if(len(mov)==2):
		m = mov[1].split(",")
		i = int(m[0])
		j = int(m[1])
		if(p_board[i][j] == 'f'):
			p_board[i][j] = '?'
		else:
			p_board[i][j] = 'f'
	else:
		m = mov[0].split(",")
		i = int(m[0])
		j = int(m[1])
		reveal_board(r_board,p_board,i,j)

def reveal_board(r_board,p_board,i,j):
	n = len(r_board)-1
	if(r_board[i][j]!=-1 and p_board[i][j]=='?'):
			p_board[i][j] = r_board[i][j]
	if(i>0):
		if(r_board[i-1][j]!=-1 and p_board[i-1][j]=='?'):
			p_board[i-1][j] = r_board[i-1][j]
	if(i>0 and j>0):
		if(r_board[i-1][j-1]!=-1 and p_board[i-1][j-1]=='?'):
			p_board[i-1][j-1] = r_board[i-1][j-1]
	if(i<n):
		if(r_board[i+1][j]!=-1 and p_board[i+1][j]=='?'):
			p_board[i+1][j] = r_board[i+1][j]
	if(i<n and j<n):
		if(r_board[i+1][j+1]!=-1 and p_board[i+1][j+1]=='?'):
			p_board[i+1][j+1] = r_board[i+1][j+1]
	if(j>0):
		if(r_board[i][j-1]!=-1 and p_board[i][j-1]=='?'):
			p_board[i][j-1] = r_board[i][j-1]
	if(i<n and j>0):
		if(r_board[i+1][j-1]!=-1 and p_board[i+1][j-1]=='?'):
			p_board[i+1][j-1] = r_board[i+1][j-1]
	if(j<n):
		if(r_board[i][j+1]!=-1 and p_board[i][j+1]=='?'):
			p_board[i][j+1] = r_board[i][j+1]
	if(i>0 and j<n):
		if(r_board[i-1][j+1]!=-1 and p_board[i-1][j+1]=='?'):
			p_board[i-1][j+1] = r_board[i-1][j+1]

n_board = int(input())
while(n_board<4 or n_board>10):
	print("Board size must be between 4 and 10!")
	n_board = int(input())
real_board = gen_board(n_board)
player_board = gen_player_board(n_board)

n_bomb = int(input())
bombs = []

for i in range(n_bomb):
	bomb = input().split(',')
	bombs.append(bomb)

reformat_board(real_board,bombs)
print("Real Board:\n")
print_real_board(real_board)

while(1):
	if(check_win(player_board)):
		print("You win!")
		break
	print("Player Board:\n")
	print_player_board(player_board)
	move= input("Your move (example : '1,3' to open or 'f 1,3' to flag) : ")
	if(validate(move)):
		mov = move.split(" ")
		if(len(mov)==1):
			m = mov[0].split(",")
			if(real_board[int(m[0])][int(m[1])] == -1):
				print("BOOM!!!")
				break
		process_move(real_board,player_board,move)
	else:
		print("Invalid move format!")