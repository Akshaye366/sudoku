import random as r

def testing():
    board= [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    completeboard= [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    def validation(posx, posy, value):
        columnSpace = True
        rowSpace = True
        squareSpace = True
        space = True
        x = 0
        y = 0
        if 3 <= posx <= 5:
            x = 3
        elif posx >= 6:
            x = 6

        if 3 <= posy <= 5:
            y = 3

        elif posy >= 6:
            y = 6

        if board[posy][posx] != 0: # Checks whether another number has taken the slot
            space = False

        for j in range(0,3):#Checks whether the number is repeated in the 3x3 grid
            for i in range(0,3):
                if board[y+j][x+i] == value:
                    squareSpace = False

        for j in range(0,9):#Checks whether the value is repeated in the column
            if board[j][posx] == value:
                columnSpace = False

        for i in range(0,9):#Checks whether the value is repeated in the row
            if board[posy][i] == value:
                rowSpace = False

        if columnSpace == False or rowSpace == False or squareSpace == False or space == False:#Considers whether value is valid or not
            return False
        else:
            return True
        
    numbers = [1,2,3,4,5,6,7,8,9]#Numbers to choose from
    posy=0
    posx=0
    invalids = 0#Invalid counter
    Sinvalids = 0#Second invalid counter

    while posy < 9:
        ind = r.randint(0,len(numbers)-1)#Selects index of random number to be added
        value = numbers[ind]#Stores value to be added
        if validation(posx, posy, value) == False:
            # Checks if position for value is valid by checking if either validation boolean is false
            posx-=1
            invalids += 1

            if invalids >= 25:
                invalids = 0
                Sinvalids +=1
                board[posy] = [0, 0, 0, 0, 0, 0, 0, 0, 0]#Resets row
                posx = -1#Starts at first position once incremented
                numbers = [1,2,3,4,5,6,7,8,9]#Resets numbers array

            if Sinvalids >= 15:
                Sinvalids = 0
                board[posy-1] = [0, 0, 0, 0, 0, 0, 0, 0, 0]#Resets previous row
                board[posy] = [0, 0, 0, 0, 0, 0, 0, 0, 0]#Resets row
                posy-=1#Move one row back
                posx = -1
                numbers = [1,2,3,4,5,6,7,8,9]
        else:
            board[posy][posx] = numbers[ind]#Updates new value in board
            numbers.pop(ind)#Removes added number from numbers array
            if posx == 8: #Starts at the next row once final index is reached
                posx=-1
                posy+=1
                numbers = [1,2,3,4,5,6,7,8,9]
        posx+=1 #Increments column

    for j in range(9): # Makes completeboard the same as board
        for i in range(9):
            completeboard[j][i] = board[j][i]
            
    return completeboard, board

testing()