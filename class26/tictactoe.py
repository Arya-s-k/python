# tic tac toe game 

board = {'7':' ' , '8':' ' , '9':' ',
         '4':' ' , '5':' ' , '6':' ',
         '1':' ' , '2':' ' , '3':' '
         }

board_keys = []

for key in board :
    board_keys.append(key)

def print_board(board):
    print(board["7"]+"|" + board["8"]+"|" + board["9"])
    print("_|_|_")
    print(board["4"]+"|" + board["5"]+"|" + board["6"])
    print("_|_|_")
    print(board["1"]+"|" + board["2"]+"|" + board["3"])
    
    
def game():
    
    turn = "X"
    count = 0
    
    for i in range(10):
        print_board(board)
        print("it is your turn",turn)
        move = input("put in your place you want to move")
        if board[move] == ' ' :
            board[move] = turn
            count+=1
        else :
            print("the board place is filled")
            continue
        
        if count >= 5 :
            if board['7'] == board['8'] == board['9'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['4'] == board['5'] == board['6'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['1'] == board['2'] == board['3'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['7'] == board['4'] == board['1'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['8'] == board['5'] == board['2'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['9'] == board['6'] == board['3'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['7'] == board['5'] == board['3'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
            elif board['9'] == board['5'] == board['1'] !=1:
                print_board(board)
                print("game over")
                print(turn , " won ")
                break
        if count == 9 :
            print("it is a tie")
            
        if turn == "X" :
            turn = "O"
        else : 
            turn = "X"
        
    restart = input("do you want o restart (y / n )" )
    if restart.lower() == "y":
        for key in board_keys:
            board[key] = " "
            
        game()

if __name__ == "__main__" : 
    game()