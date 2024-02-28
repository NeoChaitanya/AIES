import random 

def random_move(canvas,complete):

    success = False
    
    while(success != True):
        
        rand_row = random.randrange(0,3)
        rand_col = random.randrange(0,3)
        
        if(canvas[rand_row][rand_col] == '_'):
            canvas[rand_row][rand_col] = 'X'
            complete += 1
            success = True
        
       
    
def user_input(canvas,complete):
    success = False
    
    while(success != True):
        row = int(input("enter row no"))
        col = int(input("enter col no"))
        
        if ((canvas[row][col]) == '_'):
            canvas[row][col] = 'O'
            complete += 1
            success = True

        else:
            print("the cell is aldrady occupied")

        
def canvas_complete(complete):
    if(complete == 9):
        return True
    
    elif(complete < 9):
        return False
    
    else:
        print("error")
        return False

# def winner(canvas):
    
    
def print_canvas(canvas):
    for i in range(0,3):
        print(canvas[i][0], canvas[i][1], canvas[i][2])

    
def main():
    canvas = [['_','_','_'],
            ['_','_','_'],
            ['_','_','_']]

    complete = 0
    
    print("Tic Tac Toe")
    
    while(canvas_complete(complete) == False):
        random_move(canvas,complete)
        print_canvas(canvas)
        user_input(canvas,complete)
        

if __name__ == "__main__":
    main()