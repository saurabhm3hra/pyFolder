import sys


class Board:
	# TicTacToe Board
	board = {"TL": ' ', "TM": ' ', "TR": ' ',
	         "ML": ' ', "MM": ' ', "MR": ' ',
	         "LL": ' ', "LM": ' ', "LR": ' '}

	def __str__(self):
		# Print Board contents
		return self.board['TL'] + '|' + self.board['TM'] + '|' + self.board['TR'] + '\n' + \
			'-+-+-' + '\n' + self.board['ML'] + '|' + self.board['MM'] + '|' + self.board['MR'] + '\n' + \
			'-+-+-' + '\n' + self.board['LL'] + '|' + self.board['LM'] + '|' + self.board['LR']

	def CheckWin(self):
		# Check if player won
		if self.board["TL"] == "X" and self.board["TM"] == "X" and self.board["TR"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["TL"] == "O" and self.board["TM"] == "O" and self.board["TR"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["ML"] == "X" and self.board["MM"] == "X" and self.board["MR"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["ML"] == "O" and self.board["MM"] == "O" and self.board["MR"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["LL"] == "X" and self.board["LM"] == "X" and self.board["LR"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["LL"] == "O" and self.board["LM"] == "O" and self.board["LR"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["TL"] == "X" and self.board["ML"] == "X" and self.board["LL"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["TL"] == "O" and self.board["ML"] == "O" and self.board["LL"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["TM"] == "X" and self.board["MM"] == "X" and self.board["LM"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["TM"] == "O" and self.board["MM"] == "O" and self.board["LM"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["TR"] == "X" and self.board["MR"] == "X" and self.board["LR"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["TR"] == "O" and self.board["MR"] == "O" and self.board["LR"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["TL"] == "X" and self.board["MM"] == "X" and self.board["LR"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["TL"] == "O" and self.board["MM"] == "O" and self.board["LR"] == "O":
			print("Player 2 won")
			sys.exit()
		elif self.board["TR"] == "X" and self.board["MM"] == "X" and self.board["LL"] == "X":
			print("Player 1 won")
			sys.exit()
		elif self.board["TR"] == "O" and self.board["MM"] == "O" and self.board["LL"] == "O":
			print("Player 2 won")
			sys.exit()


board1 = Board()
print("Player 1: X | Player 2: O")
while True:
	p1 = input("Player 1 Turn: ")
	board1.board[p1] = "X"
	print(board1)
	board1.CheckWin()
	p2 = input("Player 2 Turn: ")
	board1.board[p2] = "O"
	print(board1)
	board1.CheckWin()
