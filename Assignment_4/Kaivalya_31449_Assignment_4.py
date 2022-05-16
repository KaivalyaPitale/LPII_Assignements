from os import system, name
import time
def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
N = int(input("Enter number of Queens: "))
Speed = int(input("Please enter calculaion speed: "))
ld = [0] * 100
rd = [0] * 100
cl = [0] * 100
#stacks
clear()


def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()


def solveNQUtil(board, col):

	if (col >= N):
		return True
	else:
		printSolution(board)
		time.sleep(1/Speed)
		clear()

	for i in range(N):

		if ((ld[i - col + N - 1] != 1 and
			rd[i + col] != 1) and cl[i] != 1):

			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

			if (solveNQUtil(board, col + 1)):
				return True
				

			board[i][col] = 0 # BACKTRACK
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

	return False
	
def solveNQ():
	board = []
	for i in range(N):
	    R = []
	    for j in range(N):
	        R.append(0)
	    board.append(R)
	if (solveNQUtil(board, 0) == False):
		print("Solution does not exist")
		return False
	printSolution(board)
	return True

solveNQ()


