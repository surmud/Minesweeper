# File: proj3.py
# Author: Surmud Jamil
          
#Constants
FLAG = "F"
MINE = "*"
BORDER = "#"
HIDDEN_CELL = "."
EMPTY_CELL = " "
REVEALED_CELL = "R"
REVEAL = "r"
FLAG_SPACE = "f"
DETONATED_MINE = "X"
POSSIBLE_CELL_NUMS = [1, 2, 3, 4, 5, 6]

# prettyPrintBoard() prints the board with row and column labels,
#                    and spaces the board out so that it looks square
# Input:             board;   the rectangular 2d gameboard to print
# Output:            None;    prints the board in a pretty way
def prettyPrintBoard(board):

    print() # empty line

    # if enough columns, print a "tens column" line above
    if len(board[0])-2 >= 10:
        print("{:25s}".format(""), end="")  # empty space for 1 - 9
        for i in range(10, len(board[0])-1 ):
            print( str(i // 10), end =" ")
        print()

    # create and print top numbered line
    print("       ", end="")
    # only go from 1 to len - 1, so we don't number the borders
    for i in range(1, len(board[0])-1 ):
        # only print the last digit (so 15 --> 5)
        print(str(i % 10), end = " ")
    print()

    # create the border row
    borderRow = "     "
    for col in range(len(board[0])):
        borderRow += board[0][col] + " "

    # print the top border row
    print(borderRow)
                         
    # print all the interior rows
    for row in range(1, len(board) - 1):
        # print the row label
        print("{:3d}  ".format(row), end="")

        # print the row contents
        for col in range(len(board[row])):
            if str(board[row][col]) == FLAG:
                # this will print the flag in black and red
                print("\033[1;30;41m" + "F" + "\033[0m", end =" ")
            else:
                print(str(board[row][col]), end = " ")
        print()

    # print the bottom border row and an empty line
    print(borderRow, "\n")

#reveal() recursively represents an island of empty space with an R (reveal) if 
#         the user clicks on an empty spot
#input - the board and the location of the piece
#output - the updated board
def reveal(solvedBoard, board, row, column):

    #check if the solved board at the row and column is not a mine
    #if it is, 'reveal' the cell and check if the pieces around that cell are
    #if a piece around it is empty, call the reveal function at that cell
    #if a cell around it is a number, reveal the number but don't call the func
    #base case - return the board when there are no empty cells around a cell

    #Base case: if there is a flag at the spot where they want to reveal, 
    #tell them to unflag first
    if board[row][column] == FLAG:
        print("\n\n\n\nYou must unflag this spot first!\n")
        return board

    #Base Case: If the spot they reveal is a number, only reveal that number
    if solvedBoard[row][column] in POSSIBLE_CELL_NUMS:
        board[row][column] = solvedBoard[row][column]
        return board

    #Recursive case: if the same location at the solved board isn't a mine  
    #or a border, reveal the cell and everything around it
    #elif solvedBoard[row][column] != MINE and solvedBoard[row][column] != BORDER:
    else:
        #reveal the cell
        board[row][column] = solvedBoard[row][column]

        #only change it to an R if the cell is empty
        if solvedBoard[row][column] == EMPTY_CELL:
            solvedBoard[row][column] = REVEALED_CELL
        

        #check all directions around the revealed cell for an empty cell, 
        #if there's one, call the function again at that location
        if solvedBoard[row + 1][column] == EMPTY_CELL:
            board = reveal(solvedBoard, board, row + 1, column)
            
        if solvedBoard[row - 1][column] == EMPTY_CELL:
            board = reveal(solvedBoard, board, row - 1, column)
            
        if solvedBoard[row][column + 1] == EMPTY_CELL:
            board = reveal(solvedBoard, board, row, column + 1)
            
        if solvedBoard[row][column - 1] == EMPTY_CELL:
           board = reveal(solvedBoard, board, row, column - 1)
            
        #check all directions for a number but only reveal the number
        #edit at 11pm:THIS WAS WORKING BEFORE BUT NOW IT ISN'T WORKING, IDK WHY!
        
        if solvedBoard[row + 1][column] != EMPTY_CELL and \
            solvedBoard[row + 1][column] != MINE and \
            solvedBoard[row + 1][column] != BORDER:

            board[row + 1][column] = solvedBoard[row + 1][column]

        if solvedBoard[row - 1][column] != EMPTY_CELL and \
            solvedBoard[row - 1][column] != MINE and \
            solvedBoard[row - 1][column] != BORDER:

            board[row - 1][column] = solvedBoard[row - 1][column]

        if solvedBoard[row][column + 1] != EMPTY_CELL and \
            solvedBoard[row][column + 1] != MINE and \
            solvedBoard[row][column + 1] != BORDER:

            board[row][column + 1] = solvedBoard[row][column + 1]

        if solvedBoard[row][column - 1] != EMPTY_CELL and \
            solvedBoard[row][column - 1] != MINE and \
            solvedBoard[row][column - 1] != BORDER:

            board[row][column - 1] = solvedBoard[row][column - 1]

        #check/ reveal diagonals
        if solvedBoard[row + 1][column - 1] != EMPTY_CELL and \
            solvedBoard[row +  1][column - 1] != MINE and \
            solvedBoard[row + 1][column - 1] != BORDER:

            board[row + 1][column - 1] = solvedBoard[row + 1][column - 1]

        if solvedBoard[row + 1][column + 1] != EMPTY_CELL and \
            solvedBoard[row +  1][column + 1] != MINE and \
            solvedBoard[row + 1][column + 1] != BORDER:

            board[row + 1][column + 1] = solvedBoard[row + 1][column + 1]

        if solvedBoard[row - 1][column + 1] != EMPTY_CELL and \
            solvedBoard[row -  1][column + 1] != MINE and \
            solvedBoard[row - 1][column + 1] != BORDER:

            board[row - 1][column + 1] = solvedBoard[row - 1][column + 1]

        if solvedBoard[row - 1][column - 1] != EMPTY_CELL and \
            solvedBoard[row -  1][column - 1] != MINE and \
            solvedBoard[row - 1][column - 1] != BORDER:

            board[row - 1][column - 1] = solvedBoard[row - 1][column - 1]

        return board


#convertToSpace() takes the R's that represent the island and converts it to 
#spaces
#input - the board before the conversion
#output - the board after the conversion
def convertToSpace(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == REVEALED_CELL:
                board[row][column] = EMPTY_CELL
    return board

#numberBoard() places numbers on the spots of the board where they belong
#input - the initial board
#output - the updated board with the numbers
def numberBoard(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            count = 0
            if board[row][column] != BORDER and board[row][column] != MINE:
               
                #scan all four directions for a mine if the given piece isn't
                #a border or a mine
                if board[row + 1][column] == MINE:
                    count = count + 1
                    
                if board[row - 1][column] == MINE:
                    count = count + 1

                if board[row][column + 1] == MINE:
                    count = count + 1

                if board[row][column - 1] == MINE:
                    count = count + 1

                if board[row + 1][column + 1] == MINE:
                    count = count + 1

                if board[row + 1][column - 1] == MINE:
                    count = count + 1

                if board[row - 1][column + 1] == MINE:
                    count = count + 1

                if board[row - 1][column - 1] == MINE:
                    count = count + 1

                #place the number down on the spot if it's not 0
                
                if count != 0:
                    board[row][column] = count

    return board

#checkDetonatedMine() checks whether or not the person detonated a mine, if
#they did, it places a big X on the board
#input - the solved board, the user board, and the coordinates
#output - returns false if they didn't detonate a mine, true if they did
def checkDetonatedMine(solvedBoard, board, row, column):
    if solvedBoard[row][column] == MINE:
        board[row][column] = DETONATED_MINE
        return board

    else:
        return False

#placeFlag() places a flag on the spot where the user wants it
#			if a flag is already there, remove it
#input - the board and the location of where they want it to be placed
#output - the updated board once the flag is placed
def placeFlag(board, row, column):

    #change it back to a hidden cell if they flag a spot that's already flagged
    if board[row][column] == FLAG:
        print("removing flag...")
        board[row][column] = ". "


    #if they try to flag a number or a space, give an error message
    if board[row][column] != FLAG and board[row][column] != HIDDEN_CELL:
        print("\n\n\n\nThis coordinate can't be flagged")

    if board[row][column] == HIDDEN_CELL:
        board[row][column] = FLAG

    return board


#countMines() counts the number of mines in the board
#             input - the solved board
#             output - the total number of mines in the board
def countMines(solvedBoard):
    mineCount = 0
    for i in range(len(solvedBoard)):
        for j in  range(len(solvedBoard[i])):
            if solvedBoard[i][j] == MINE:
                mineCount = mineCount + 1

    return mineCount


#minesLeft() returns the number of how many mines are left that need to be found
#input - the board, the solved board, and the number of mines there are total
#output - the number of mines left
def minesLeft(board, solvedBoard, totalMines):
    #find the number of flags placed on the user board
    numFlags = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == FLAG:
                numFlags += 1

    numLeft = totalMines - numFlags
    return numLeft


#checkWin() checks for a win by seeing if the flags are in the correct spots 
#input - the board and the solved board
#output - True or false, whether or not they won
def checkWin(board, solvedBoard):
    #create a list of all of the flag locations and a list of the mine locations
    #if the lists are the same, then it means that they won
    flagList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == FLAG:
                flagList.append(i)
                flagList.append(j)

    mineList = []
    for row in range(len(solvedBoard)):
        for col in range(len(solvedBoard[row])):
            if solvedBoard[row][col] == MINE:
                mineList.append(row)
                mineList.append(col)

    if flagList == mineList:
        return True

    else:
        return False
#deepCopy() takes a 2D list and creates a deep copy of it
#input - the initial list
#ouput - the deep copied list
def deepCopy(firstList):
  newList = []
  newListRow = []
  for i in range(len(firstList)):
    newListRow = list(firstList[i])
    newList.append(newListRow)
  return newList

#createBoard() takes the list of strings from the file and turns it into a 2d
# list which represents the board
# input - board, the list of strings after the lines are read
# output - newBoard, the 2d list that will be used
def createBoard(board):
    # list looks something like [xxxxx/n, xxxxx/n, xxxxxx/n] at this point
    newBoard = []
    #scan each element in the list and append it to a new one
    for i in range(len(board)):
        newBoardRow = []
        for j in range(len(board)):
            if board[i][j] != "/" and board[i][j] != "n":
                newBoardRow.append(board[i][j])
        newBoard.append(newBoardRow)

    return newBoard


def main():

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("This program allows you to play Minesweeper.")
    print("The object of the game is to flag every mine,")
    print("using clues about the number of neighboring ")
    print("mines in each field.  To win the game, flag ")
    print("all of the mines (and don't incorrectly flag ")
    print("any non-mine fields).  Good luck!\n\n\n\n\n\n\n")


    #read in the board
    #store the board
    fileName = input("Enter the name of the minesweeper board file: ")
    boardFile = open(fileName)
    boardFileList = boardFile.readlines()
    boardFile.close()
    solvedBoard = createBoard(boardFileList)
	
    #create the user board by making a deep copy of the gameBoard and stripping
    #the asteriks
    userBoard = deepCopy(solvedBoard)
    for i in range(len(userBoard)):
        for j in range(len(userBoard[i])):

            #set all slots in the user board to a dot unless it's on the border
            if userBoard[i][j] != BORDER:
                userBoard[i][j] = HIDDEN_CELL

   

	#fill the board with the clues/numbers
    solvedBoard = numberBoard(solvedBoard)
    solvedBoardCopy = deepCopy(solvedBoard)
    userBoard =  convertToSpace(userBoard)

    #find the number of rows and columns 
    numRows = len(userBoard)
    numColumns = len(userBoard[0])


    print("There are a total of", countMines(solvedBoard), "mines")
    numMines = countMines(solvedBoard)

    gameOver = False 
	#while the game isn't over:
    while gameOver == False:
        prettyPrintBoard(userBoard)

        row = int(input("Please enter the row: "))

        #validate row input
        while row < 1 or row > (numRows - 2):
            print("Row must be between 1 and", numRows - 2)
            row = int(input("Please enter the row: "))

        column = int(input("Please enter the column: "))

        #validate column input
        while column < 1 or column > (numColumns - 2):
            print("Column must be between 1 and", numColumns - 2)
            column = int(input("Please enter the column: "))

        revealOrFlag = input("Enter an 'r' to reveal or 'f' to flag the space: ")

        #validate input
        while revealOrFlag != REVEAL and revealOrFlag != FLAG_SPACE:
            print("That's not a valid action.")
            revealOrFlag = input("Enter an 'r' to reveal or 'f' to flag the space: ")


        if revealOrFlag == REVEAL:
            
            #if a mine is detonated when they reveal a piece, end the game
            if checkDetonatedMine(solvedBoard, userBoard, row, column) != False:
                userBoard = checkDetonatedMine(solvedBoard, userBoard, row, column)
                prettyPrintBoard(userBoard)
                print("\n\n\nYou're trash, you detonated a mine! Game over!")
                gameOver = True

            #if not, reveal the piece
            else:
                userBoard = reveal(solvedBoardCopy, userBoard, row, column)
                userBoard =  convertToSpace(userBoard)

        if revealOrFlag == FLAG_SPACE:
            #if there is already a flag there, remove it
            if userBoard[row][column] == FLAG:
                userBoard[row][column] = HIDDEN_CELL
                print("\nFlag removed!")
            #if not, call the place flag function
            else:
                board = placeFlag(userBoard, row, column)

        if checkWin(userBoard, solvedBoard) == True:
            print("\n\nCongratulations! You win!")
            gameOver = True

        print("There are", minesLeft(userBoard, solvedBoard, numMines), \
                "mines left")

main()





















