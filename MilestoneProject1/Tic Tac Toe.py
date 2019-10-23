def display_board(board):
    import os
    os.system('cls')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def checkWin(L):
    if test[1]==test[2]==test[3]==L:
        return True
    if test[4]==test[5]==test[6]==L:
        return True
    if test[7] == test[8] == test[9] == L:
        return True
    if test[1] == test[5] == test[9] == L:
        return True
    if test[3] == test[5] == test[7] == L:
        return True
    if test[1] == test[4] == test[7] == L:
        return True
    if test[2] == test[5] == test[8] == L:
        return True
    if test[3] == test[6] == test[9] == L:
        return True
    else:
        return False


test=['#','1','2','3','4','5','6','7','8','9']

def player_input():
    ply=0
    player1=1
    player2=2
    i=0
    while(1):
       if i%2==0:
           player1 = int(input('Please enter a number player 1 '))
           if test[player1] != 'X' and test[player1] != 'O':
               i = i + 1
               test[player1] = 'X'
               display_board(test)
           else:
               print("Please Enter a valid number")
               continue
           if checkWin('X')==True:
               print("Player 1 win")
               break
       else:
           player2=int(input('Please enter a number player 2 '))
           if test[player2]!='X' and test[player2]!='O':
               i = i + 1
               test[player2] = 'O'
           else:
               print("Please Enter a valid number")
               continue
           display_board(test)

           if checkWin('O')==True:
               print("Player 2 win")
               break

display_board(test)
player_input()