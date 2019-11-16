import random

def display_board(board):
    print("   |   | ")
    print(" " + board[0] + " |" + " " + board[1] + " |" + " " + board[2]) 
    print("___|___|___")
    print("   |   | ")
    print(" " + board[3] + " |" + " " + board[4] + " |" + " " + board[5])
    print("___|___|___")
    print("   |   | ")
    print(" " + board[6] + " |" + " " + board[7] + " |" + " " + board[8])
    print("   |   | ")
    
    
test_board = ['a', 'b', 'x', 'd', 'x', 'f', ' g', 'h', ' ']


#display_board(test_board)

def player_input():
  marker = input("wanna be x or o")

  while not (marker == 'o' or marker == "O" or marker == "x" or marker == "X"):
    marker = input("wanna be x or o")
  
  if marker == 'o' or marker == 'O':
    return ('O', 'X')

  if marker == 'x' or marker == 'X':
    return ('X', 'O')

#removed this because ur done testing this function
#print(player_input())

#put your place_marker() function def here
def place_marker(board, marker, position):
  board[position] = marker


#put your two test calls to place_marker() and display_board() here
#this one calls place_marker and feeds in 
#test_board, '$' as the marker, and 8 as position
#place_marker(test_board,'$',8)

#this one calls display board and feeds in
#test board.  display board will print out
#test_board so you can check if place_marker updated
#the marker
#display_board(test_board)

#put win_check function here
def win_check(board, mark):

  if ((board[0] == mark and board[1] == mark and board [2] == mark) or
  (board[3] == mark and board[4] == mark and board [5] == mark) or
  (board[6] == mark and board[7] == mark and board [8] == mark) or
  (board[0] == mark and board[3] == mark and board [6] == mark) or
  (board[1] == mark and board[4] == mark and board [7] == mark) or
  (board[2] == mark and board[5] == mark and board [8] == mark) or
  (board[0] == mark and board[4] == mark and board [8] == mark) or
  (board[2] == mark and board[4] == mark and board [6] == mark)):
    return True
  else:
    return False

#test print, should print out True if win
#False if not
#this feeds in test_board and 'X' as the marker
#into win_check, then prints whatever win_check
#returns
#print(win_check(test_board,'x'))

def choose_first():
  if random.randint(0,1) == 0:
    return 'player 1'
  else:
    return 'player 2'

###print(choose_first())

def space_check(board, position):
  if board[position] == ' ':
    return True
  
  else:
    return False

#space_check takes in a whole board and a position on that board
#board position is an integer, board[0] returns the data at board position 0 ye
#missing one thing on your test line passed ayyy
#print(space_check(test_board,1))


def full_board_check(board):
  #comment out 'pass' when you start writing your code here
  for space in board:
    if space == " ":
      return False

  return True
  
      
#print(full_board_check(test_board))


#heres an example of a for loop going through a list
#just play around with it and then comment it out when u start 
#writing full_board_check()
#my_list = ['a', 'b', 'a', 'b', 'a', 'b']

#this first line goes through each item in my_list
#and temporarily stores each item as the variable name that i chose
#'item_in_list'
#for item_in_list in my_list:
  #then here it does a conditional check each time for each item
  #if the current item is equal to 'a'
  #if item_in_list == 'a':
    #print it out
    #print('i see an a')

#then once the loop is over do this
#print('Done')

def player_choice(board):
  position = int(input('what position dawg (0-8)'))

  while position not in range(0,9) or not space_check(board,position): 
   position = int(input('not available. pick something else'))
  
  return position

#print(player_choice(test_board))

def replay():
  again = input('wanna play again')
  if again == 'yes':
    return True
  else:
    return False
#print (replay())

print('welcome to tic tac toe!')

while True:
  new_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  display_board(new_board)
  #ask player 1 which marker they want
  player1_marker, player2_marker = player_input()
  
  turn = choose_first()
  print(turn + ' will go first')

  game_on = True

  while game_on:
    display_board(new_board)
    if turn == 'player 1':
      print('player 1')
      #asks which position to place marker
      position = player_choice(new_board)
      #place marker to actually update the board
      place_marker(new_board, player1_marker, position)
      if win_check(new_board, player1_marker):
        print('winner')
        display_board(new_board)
        game_on = False
      elif full_board_check(new_board):
        print('game over: draw')
        display_board(new_board)
        game_on = False
      else:
        turn = 'player 2' 
        

    else:
      print('player 2')
      position = player_choice(new_board)
      #place marker to actually update the board
      place_marker(new_board, player2_marker, position)
      if win_check(new_board, player2_marker):
        print('winner')
        display_board(new_board)
        game_on = False
      elif full_board_check(new_board):
        print('game over: draw')
        display_board(new_board)
        game_on = False
      else:
        turn = 'player 1' 

  if not replay():
     break
