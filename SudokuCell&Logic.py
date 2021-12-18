import turtle
import random

t=turtle.Turtle()

gamestate = []
startposition = []
semistartlist = []
playername = ""
leves = []
number = []

originalboard = [1,2,3,4,5,6,7,8,9,
                 4,5,6,7,8,9,1,2,3,
                 7,8,9,1,2,3,4,5,6,
                 2,3,4,5,6,7,8,9,1,
                 5,6,7,8,9,1,2,3,4,
                 8,9,1,2,3,4,5,6,7,
                 3,4,5,6,7,8,9,1,2,
                 6,7,8,9,1,2,3,4,5,
                 9,1,2,3,4,5,6,7,8]

completeboard = []

def resetboard():
    global gamestate
    gamestate = []
    for i in range(81):
        gamestate.append(0)

def resetstart():
    global startposition
    startposition = []
    for i in range(81):
        startposition.append(0)

def drawboard():
    global t
    t.ht()
    turtle.tracer(0)
    t.clear()

#External square
    t.pencolor("#000000")
    t.up()
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.goto(135,135)
    t.down()
    t.goto(135,-135)
    t.goto(-135,-135)
    t.goto(-135,135)
    t.goto(135,135)
    t.end_fill()

#Microgrids Vertical
    t.pencolor("#AAAAAA")

    t.up()
    t.goto(-105,135)
    t.down()
    t.goto(-105,-135)

    t.up()
    t.goto(-75,135)
    t.down()
    t.goto(-75,-135)

    t.up()
    t.goto(-15,135)
    t.down()
    t.goto(-15,-135)

    t.up()
    t.goto(15,135)
    t.down()
    t.goto(15,-135)

    t.up()
    t.goto(75,135)
    t.down()
    t.goto(75,-135)

    t.up()
    t.goto(105,135)
    t.down()
    t.goto(105,-135)
    
#Microgrids Horizontal
    t.up()
    t.goto(135,-105)
    t.down()
    t.goto(-135,-105)

    t.up()
    t.goto(135,-75)
    t.down()
    t.goto(-135,-75)

    t.up()
    t.goto(135,-15)
    t.down()
    t.goto(-135,-15)

    t.up()
    t.goto(135,15)
    t.down()
    t.goto(-135,15)

    t.up()
    t.goto(135,75)
    t.down()
    t.goto(-135,75)

    t.up()
    t.goto(135,105)
    t.down()
    t.goto(-135,105)

#Macrogrids
    t.pencolor("#000000")
    t.up()
    t.goto(45,135)
    t.down()
    t.goto(45,-135)

    t.up()
    t.goto(-45,135)
    t.down()
    t.goto(-45,-135)

    t.up()
    t.goto(-135,45)
    t.down()
    t.goto(135,45)

    t.up()
    t.goto(-135,-45)
    t.down()
    t.goto(135,-45)

#Text
    t.pencolor("#4477FF")
    t.up()
    t.goto(0,200)
    t.down()
    t.write("Project.SUDOKU", align="center", font=("Arial", 30, "bold"))
    t.up()
    t.goto(0,170)
    t.down()
    t.write("Programmed by Amal and Jianli", align="center", font=("Arial", 12))
    t.up()
    t.goto(135,-155)
    t.down()
    t.write("Python Programming Project - Spring 2018", align="right", font=("Arial", 7))
    t.up()
    t.goto(0,-220)
    t.down()
    t.write("To play the game, enter the difficulty in the shell.\nEnter 'Help' to read the instructions.", align="center", font=("Arial", 10))

#Map coordinates

    t.pencolor("#DD3322")
    t.up()
    t.goto(-120,145)
    t.down()
    t.write("1x", align = "center")

    t.up()
    t.goto(-90,145)
    t.down()
    t.write("2x", align = "center")

    t.up()
    t.goto(-60,145)
    t.down()
    t.write("3x", align = "center")

    t.up()
    t.goto(-30,145)
    t.down()
    t.write("4x", align = "center")

    t.up()
    t.goto(0,145)
    t.down()
    t.write("5x", align = "center")

    t.up()
    t.goto(30,145)
    t.down()
    t.write("6x", align = "center")

    t.up()
    t.goto(60,145)
    t.down()
    t.write("7x", align = "center")

    t.up()
    t.goto(90,145)
    t.down()
    t.write("8x", align = "center")

    t.up()
    t.goto(120,145)
    t.down()
    t.write("9x", align = "center")

#

    t.up()
    t.goto(-155,115)
    t.down()
    t.write("1y", align = "center")

    t.up()
    t.goto(-155,85)
    t.down()
    t.write("2y", align = "center")

    t.up()
    t.goto(-155,55)
    t.down()
    t.write("3y", align = "center")

    t.up()
    t.goto(-155,25)
    t.down()
    t.write("4y", align = "center")

    t.up()
    t.goto(-155,-5)
    t.down()
    t.write("5y", align = "center")

    t.up()
    t.goto(-155,-35)
    t.down()
    t.write("6y", align = "center")

    t.up()
    t.goto(-155,-65)
    t.down()
    t.write("7y", align = "center")

    t.up()
    t.goto(-155,-95)
    t.down()
    t.write("8y", align = "center")

    t.up()
    t.goto(-155,-125)
    t.down()
    t.write("9y", align = "center")

    
    t.up()
    
    turtle.update()

#board's logic
    
def fillboard():
    global gamestate

    for i in range(81):
        fillcell(i,gamestate[i])


def fillcell(position,state):
    global t
    t.up()
    t.goto(turtlecoord(chesscoord(position))[0],turtlecoord(chesscoord(position))[1])
    if state != 0:
        t.pencolor("#4477FF")
        t.right(90)
        t.forward(10)
        t.left(90)
        t.write(str(state))
        
    turtle.update()

def chesscoord(n):
    x = n%9
    y = int(n/9)

    coord = [x,y]

    return coord

def inversechesscoord(list):
    itemposition = (list[0]-1)+(list[1]-1)*9

    return itemposition

def turtlecoord(list):
    x = -90 + 30*(list[0]-1)
    y = 90 - 30*(list[1]-1)

    coord = [x,y]

    return coord

#all the formulae for the permutation of the game

def originalboardshuffle():
    global completeboard
    global originalboard
    blockhorizontal(random.randint(5,10))
    blockvertical(random.randint(5,10))
    linehorizontal(random.randint(5,10))
    linevertical(random.randint(5,10))
    completeboard = originalboard

def blockhorizontal(n1):
    global originalboard
    
    for i in range(n1):

        temporaryboard = originalboard[:]
        permutation1 = [random.randint(1,3)]
     
        permutation2 = [1,2,3]
        permutation2 = list(set([1,2,3]) - set(permutation1))
        random.shuffle(permutation2)

        for p in range(27):
            temporaryboard[(permutation1[0]-1)*27+p] = originalboard[(permutation2[0]-1)*27+p]
            temporaryboard[(permutation2[0]-1)*27+p] = originalboard[(permutation1[0]-1)*27+p]      
        
        originalboard = temporaryboard

def blockvertical(n2):
    global originalboard
    
    for i in range(n2):

        temporaryboard = originalboard[:]
        permutation1 = [random.randint(1,3)]
        permutation2 = [1,2,3]
        permutation2 = list(set([1,2,3]) - set(permutation1))
        random.shuffle(permutation2)
        for p in range(27):
            temporaryboard[(permutation1[0]-1)*3+p%3+int(p/3)*9] = originalboard[(permutation2[0]-1)*3+p%3+int(p/3)*9]
            temporaryboard[(permutation2[0]-1)*3+p%3+int(p/3)*9] = originalboard[(permutation1[0]-1)*3+p%3+int(p/3)*9]

        originalboard = temporaryboard

def linehorizontal(n3):
    global originalboard

    for i in range(n3):

        temporaryboard = originalboard[:]
        permutation1 = [random.randint(1,3)]
     
        permutation2 = [1,2,3]
        permutation2 = list(set([1,2,3]) - set(permutation1))
        random.shuffle(permutation2)
        permutation3 = [random.randint(1,3)]

        for p in range(9):
            temporaryboard[(permutation1[0]-1)*9+p+(permutation3[0]-1)*27] = originalboard[(permutation2[0]-1)*9+p+(permutation3[0]-1)*27]
            temporaryboard[(permutation2[0]-1)*9+p+(permutation3[0]-1)*27] = originalboard[(permutation1[0]-1)*9+p+(permutation3[0]-1)*27]      
        
        originalboard = temporaryboard

def linevertical(n4):
    global originalboard
    
    for i in range(n4):
        temporaryboard = originalboard[:]
        permutation1 = [random.randint(1,3)]
        permutation2 = [1,2,3]
        permutation2 = list(set([1,2,3]) - set(permutation1))
        random.shuffle(permutation2)
        permutation3 = [random.randint(1,3)]

        for p in range(9):
            temporaryboard[(permutation1[0]-1)+int(p)*9+(permutation3[0]-1)*3] = originalboard[(permutation2[0]-1)+int(p)*9+(permutation3[0]-1)*3]
            temporaryboard[(permutation2[0]-1)+int(p)*9+(permutation3[0]-1)*3] = originalboard[(permutation1[0]-1)+int(p)*9+(permutation3[0]-1)*3]

        originalboard = temporaryboard

#defining the gameboard

def semistart(difc):
    global semistartlist

    semistartlist = []
    for i in range(81):
        semistartlist.append(0)
    n = 0
    while n < difc:
        semistartlist[random.randint(0,80)]=1
        n = sum(semistartlist)
        
def startstate():
    global semistartlist
    global originalboard
    global startposition

    for i in range(81):
        if semistartlist[i] == 1:
            startposition[i] = originalboard[i]

#define the player's username
            
def neoplayer():
    global playername
    drawboard()
    playername = input("Enter your name: ")

#choose levels
            
def gamestarter():
    global gamestate
    global startposition
    global neoplayer
    
    drawboard()
    z = 0

    while z == 0:
        leves = input("Enter 'A' for Easy, 'B' for Medium and 'C' for Hard mode: ").upper()
        if leves == "A":
            Val = 60
            t.clear()
            resetboard()
            resetstart()
            originalboardshuffle()
            semistart(Val)
            startstate()
            gamestate = startposition[:]
            drawboard()
            fillboard()
            z = 1
        elif leves == "B":
            Val = 45
            t.clear()
            resetboard()
            resetstart()
            originalboardshuffle()
            semistart(Val)
            startstate()
            gamestate = startposition[:]
            drawboard()
            fillboard()
            z = 1
        elif leves == "C":
            Val = 30
            t.clear()
            resetboard()
            resetstart()
            originalboardshuffle()
            semistart(Val)
            startstate()
            gamestate = startposition[:]
            drawboard()
            fillboard()
            z = 1
        elif leves == "SUPER EASY MODE":
            Val = 80
            t.clear()
            resetboard()
            resetstart()
            originalboardshuffle()
            semistart(Val)
            startstate()
            gamestate = startposition[:]
            drawboard()
            fillboard()
            z = 1
        elif leves == "HELP":
            print("   ******************* Informations *******************")
            print("a) To play the game, you must first enter the A, B or C to choose the level of difficulty.")
            print("b) After that, you have to insert coordinates x(row) and y(column), both are number from 1 to 9.\n   (for example, 11 for the cell on the top left or 55 for the very center cell)")
            print("c) Then, you have to put a number from 1 to 9 as your answer,\n   put any other numbers if you want to come back.")
            print("d) You can overwrite your own answers.")
            print("e) Enter 'RESET' to restart the game with a new player.")
            print("f) Once you think you have done, enter 'CHECK' to see if your answers are right.")
            print("g) You can save your progresses in an external file by entering 'SAVE',\n   but you cannot load it... we are not good enough for that.")
            print("h) Since this is a random system, there may be more than one answer for our Sudoku,\n   if you are sure that your answers is right, well, blame the developers of this game.")
            print("i) You can clean all your inputs by entering 'CLEAR', the game will be the same, but you will erase all our answers.")
            print("   ****************** Enjoy the game ******************")
            z = 0
        else:
            leves = input("Input not valid - Enter anything to come back to level selection: ").upper()
            z = 0
        
#playing
            
def userinput():
    global semistarlist
    global gamestate
    global startposition
    global completeboard
    global playername
    p = 0

    

    while p == 0:
        commands = input("Enter your commands or coordinates(xy): ").upper()
        
        #reset the game
        if commands == "RESET":
            print("A new player is ready to play.")
            t.clear()
            
            p = 1

            main()
                    
        #check if the answers are right            
        elif commands == "CHECK":
            if gamestate == completeboard:
                print("Congratulation! You have completed the level!\nYour board has been saved in the file SudokuVictoriesBoard.txt.")

                file = open("SudokuVictoriesBoard.txt","w")
                
                file.write(playername)
                file.write("\nThe 0s represent the empty cells.\n")
                file.write("\nThe completed board:\n")
                file.write(str(gamestate))
                file.write("\nThe original game:\n")
                file.write(str(startposition))

                file.close()
                
                p = 1
                
                main()
            elif gamestate != completeboard:
                print("The game is not complete, there is something wrong or missing!")
                
                p = 0

        #clean the user inputted numbers from the board
        elif commands == "CLEAR":
            gamestate = startposition[:]
            drawboard()
            fillboard()

            
            p = 0
        
        #save the progress but they cannot be reloaded in the game
        elif commands == "SAVE":

            file = open("SudokuUserInputs.txt","w")

            file.write(str(playername))
            file.write("\nThe 0s represent the empty cells.\n")
            file.write("\nThe original game:\n")
            file.write(str(startposition))
            file.write("\nThe user's inputs:\n")
            file.write(str(gamestate))
            file.write("\nThe solution of this game:\n")
            file.write(str(completeboard))

            file.close()
            print("You have successfully saved the file, you can find also the complete board inside: do not cheat please.\nThe file name is 'SudokuUserInputs.txt, you can find it in the same folder where you opened this file.")
            p = 0
            
        #helping
        elif commands == "HELP":
            print("   ******************* Informations *******************")
            print("a) To play the game, you must first enter the A, B or C to choose the level of difficulty.")
            print("b) After that, you have to insert coordinates x(row) and y(column), both are number from 1 to 9.\n   (for example, 11 for the cell on the top left or 55 for the very center cell)")
            print("c) Then, you have to put a number from 1 to 9 as your answer,\n   put any other numbers if you want to come back.")
            print("d) You can overwrite your own answers.")
            print("e) Enter 'RESET' to restart the game with a new player.")
            print("f) Once you think you have done, enter 'CHECK' to see if your answers are right.")
            print("g) You can save your progresses in an external file by entering 'SAVE',\n   but you cannot load it... we are not good enough for that.")
            print("h) Since this is a random system, there may be more than one answer for our Sudoku,\n   if you are sure that your answers is right, well, blame the developers of this game.")
            print("i) You can clean all your inputs by entering 'CLEAR', the game will be the same, but you will erase all our answers.")
            print("   ****************** Enjoy the game ******************")

            p = 0

        #the following is the playing set up, after the player gives the coordinates, the player has to put the answer  
        elif len(commands) == 2:  
            if (int(commands) < 100) and (int(commands)%10 != 0) and (int(commands) > 10):
                x = int(int(commands)/10)
                y = int(commands)%10
                coord = [x,y]
                n = inversechesscoord(coord)
                if semistartlist[n] == 1:
                    print("This is a given cell: you can't fill it.")
                    p = 0
                elif semistartlist[n] == 0:
                    number = input("Input your answer (1 to 9): ")
                    if number == "1":
                        gamestate[n] = 1
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "2":
                        gamestate[n] = 2
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "3":
                        gamestate[n] = 3
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "4":
                        gamestate[n] = 4
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "5":
                        gamestate[n] = 5
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "6":
                        gamestate[n] = 6
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "7":
                        gamestate[n] = 7
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "8":
                        gamestate[n] = 8
                        drawboard()
                        fillboard()
                        p = 0
                    elif number == "9":
                        gamestate[n] = 9
                        drawboard()
                        fillboard()
                        p = 0
                    else:
                        print("Input for answer cancelled.")
                        p = 0
                        
        #when the input is not correct
        else:
            print("Wrong command, input 'HELP' to understand how to play.")
            p = 0
        
def main():
    neoplayer()
    gamestarter()
    userinput()

main()
