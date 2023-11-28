# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
checkers_board= []
for __x in range(8):
    checkers_board.append([" "," "," "," "," "," "," "," "])
checkers_board[1][2]="P12R"
board =checkers_board
color="R"
#print(checkers_board)
board_set=set()
occupied_squares=set()
red_squares=set()
black_squares=set()
#for row in range(8):
    #avaliable_squares.append((board[row][(((row%2)+1)%2)::2]))
    #print(avaliable_squares)
    #for position in range(4):
        #print("hi")
        #print(board[row][(row%2)::2])
def amount_of_pieces(board):
    indexes = color_indexes(board)
    return (len(indexes[0])+len(indexes[1]))
def list_of_color(board,color):
    if color == "R":
        print("is red")
        return color_indexes(board)[0]
    print("not red")
    return color_indexes(board)[1]
def color_indexes(board):
    #return 2d list. red is index[0] black is index[1]
    red_list=[]
    black_list=[]
    for row in range(8):
        for __x in (board[row][(((row%2)+1)%2)::2]):
            if "R" in __x:
                red_list.append(__x)
            if "B" in __x:
                black_list.append(__x)
    return [red_list,black_list]
def piece_type(pieces):
    #returns set
    king_set=set()
    pawn_set = set(pieces)
    for __z in range(len(pieces)):
        if "K" == __z[0]:
            king_set.add(__z)
    pawn_set.difference_update(king_set.copy())
    if king_set == set():
        king_set = None
    return pawn_set,king_set
          
def jump_is_available(board,color):
    #returns True or false
    #p.s. black is always up
    all_pieces = color_indexes(board)
    if color == "R":
        opposite_color = "B"
        my_pieces= all_pieces[0]
        opponents_pieces= all_pieces[1]
        board_check_dir = -1
    else:
        opposite_color = "R"
        my_pieces= all_pieces[1]
        opponents_pieces= all_pieces[0]
        board_check_dir = 1
    #for __item in my_pieces:
        
        
        
            
        
        
        
                

        

    
        
    
        
        
#def amount_of_pieces(board):
    #for row in range(8):
        #for __x in (board[row][(((row%2)+1)%2)::2]):
            #board_set.add(__x)
            #if "R" in __x:
                #print(__x)
                #occupied_squares.add(__x)
                #red_squares.add(__x)
            #if "B" in __x:
                #black_squares.add(__x)    
#def available_moves(    
                    
    #print(avaliable_squares)
            #print("hi")
            #print(board[row][(row%2)::2])
        #print (board[row][(row+1):2:],(row%2))
        #if color in board[row][(row%2):2:]:
            #print (board[row][(row%2):2:],"here")
   # return 8

    
#def red_pawn_moves(board):
    #if 


    #def red_king_moves(board):
    

#def main(board,color):

        
    




#print(1%2)
#main(checkers_board,"R")
print(amount_of_pieces(checkers_board))
print(occupied_squares,red_squares,black_squares,board_set)
print(color_indexes(board))
print(jump_is_available(board,color))
