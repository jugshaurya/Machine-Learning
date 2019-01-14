'''
To clear the screen between moves in jupyter notebook:


    from IPython.display import clear_output
    clear_output()
''' 

from IPython.display import clear_output

def display_board(board):
	clear_output()
	print('Status Of Board: \n')
	print("        " + board[7] +'|' + board[8] + '|' + board[9])
	print("        " + '-' +'|' + '-' + '|' + '-')
	print("        " + board[4] +'|' + board[5] + '|' + board[6])
	print("        " + '-' +'|' + '-' + '|' + '-')
	print("        " + board[1] +'|' + board[2] + '|' + board[3])

def is_won(board,mark):


	# checking all Rows
	if (board[1]==board[2]==board[3]==mark or
		board[4]==board[5]==board[6]==mark or
		board[7]==board[8]==board[9]==mark) :
		return True


	# checking all Cols
	if (board[1]==board[4]==board[7]==mark or
		board[2]==board[5]==board[8]==mark or 
		board[3]==board[6]==board[9]==mark ):
		return True

	# checking both Diagonals
	if (board[1]==board[5]==board[9]==mark or
		board[3]==board[5]==board[7]==mark) :
		return True

	return False
	
def toggle(next_player,next_symbol):

	'''
		DOCSTRING
		next_ player : value is either 1 or 2
		next_symbol  : value is either 'X' or 'O' 

		OUTPUT : returns tuple (next_player,next_symbol)
	'''
	if (next_player == 1 ):
		next_player = 2
	else:
		next_player = 1

	if next_symbol=='X':
		next_symbol = 'O'
	else:
		next_symbol ='X'
	return (next_player,next_symbol)


# starting of program
if( __name__ == '__main__'):

	#defining empty board
	board = [str(x) for x in range(10)]

	# Taking player1 choice of 'X' or 'O'
	XorO = input("Do you want X or O?: ")
	while(XorO !='X' and XorO!='O'):
		XorO = input("Please choose 'X' or 'O' !")

	# Printing player1 choice of 'X' or 'O'
	print("You got {}".format(XorO))

	#initals
	player = 1 # players are [1,2]
	ch = XorO  # ch can be any in ['X' ,'O']
	
	for x in range(10):
		display_board(board)
		
		if x == 9:
			print("Match Tied!")
			break
		
		# Taking Input of Board Position  
		while(True):
			index = int(input("Enter the position(1-9) for Player {} : ".format(player)))
			if int(board[index]) == index:
				board[index] = ch	
				break
			else:
				print("Enter the position that is Empty")	

		# won_check
		if is_won(board,ch):
			display_board(board)
			print(f"Player {player} win ")
			break
		else:
			pass

		#Toggle
		player, ch = toggle(player, ch)