## Nim game
# This program produces Nim game for 2 players or for a palyer vs computer

# import modules
from random import randint
from random import choice
from time import sleep

def main():
    # welcome message and brief instrucitons
    printIntro()
    
    ## initializing variables
    counter=0
    
    # user input - creating piles
    piles=createPiles()
    
    # calculating total of tokens and assigning to a variable
    totalTokens=sumOfTokens(piles)
    
    ## printing available piles
    printPiles(piles)
    
    ## user input - choosing an opponent
    players=choosePlayer()

    ##game starts
    # visual border and "Game starts" message
    printBorderStart()
    # players exchanging their moves
    while totalTokens >0:
        # counting moves to determine which player's turn it is
        counter = countMoves(counter) 
        currentPlayer = assignCurrentPlayer(players,counter)
        printWhoseTurn(currentPlayer)
        pilesIndices = listActivePilesIndices(piles)
        if currentPlayer == "Computer":
            pileIndexAndQty = computerMove(piles,pilesIndices)
            printCompThinking()
            printComputerMove(pileIndexAndQty)
            sleep(4)
        else:
            pileIndexAndQty = userMove(piles,pilesIndices)
        piles = pilesUpdate(piles, pileIndexAndQty)
        totalTokens=sumOfTokens(piles)
        printPiles(piles)
        
    # print who is the winner and Game over
    printGameOver(currentPlayer)


#################################### Functions are defined below #####################################
    
#################################### 1. Functions updating objects, prompting for user input and returning values ##############################


# the function below creates piles with tokens as per user's input
# it returns piles, a list of piles with tokens chosen at the begining of the game
def createPiles():
    #initializing a variable
    piles=[]
    # user input for number of required piles
    numberOfPiles=int(input("\nHow many piles do you want in the game? "))

    # user enters number of tokens for each pile
    print("Enter tokens quantity for each pile followed by ENTER: ")
    for i in range(numberOfPiles):
        tokens=input("")
        piles.append(int(tokens))
    return piles

# this function takes user input on who will play in the game - player vs palayer OR player vs computer
#@param players, a list of players in the game
# it returns players, the updated list of players
def choosePlayer():
    #initializing a variable
    players=["Player 1"] 
    #user input
    addPlayer=input('\nWho do you want to play against? (Enter "P" for Player 2 or "C" for Computer): ').upper()

    #input validation
    while addPlayer not in ["C","P"]:
        addPlayer=input('Incorrect entry. \nWho do you want to play against? (Enter "P" for Player 2 or "C" for Computer): ').upper()
        
    #adding a new player to the list of players   
    if addPlayer=="C":
        players.append("Computer")
    else:
        players.append("Player 2")
    return players

## the function adds up number of turns
# @param counter
# returns the updated counter
def countMoves(counter):
    counter=counter+1
    return counter

## the function  computes whose turn it is
# @param players, list of players
# @param counter
# returns currentPlayer, the player whose turn it is
def assignCurrentPlayer(players,counter):
    # odd number: Player 1's turn, even number Player 2's or Computer's turn (depends on the game type)
    if counter %2==1:
        currentPlayer = players[0]
    else:
        currentPlayer=players[1]
    return currentPlayer


# the function lists indices for piles with tokens qty >0
# @param piles
# returns pilesIndices, positions of the actual piles in the list
def listActivePilesIndices(piles):
    pilesIndices= [i for i in range(len(piles)) if piles[i]>0]
    return pilesIndices

## function prompting user to remove tokens
# it doesn't allow to pick empty piles
# it doesn't allow to pick less than ZERO or more than available tokens qty in the chosen pile
# @param piles
# @param pilesIndices

def userMove(piles,pilesIndices):
    # listing actual piles numbers where tokens qty > 0
    availablePiles=[i+1 for i in pilesIndices]
    
    # prompting user for an input to pick a pile
    print("Choose a pile number from the following:",availablePiles,":")
    chosenPile=int(input())
    
    # validating the input for chosen pile
    while chosenPile not in availablePiles:
        print("Invliad entry.")
        print("Choose a pile from the list",availablePiles,":")
        chosenPile=int(input())

    # finding the chosen pile index
    chosenPileIndex = chosenPile-1
        
    # finding token qty of the chosen pile
    pileQty= piles[chosenPileIndex]

    # updating the players choice: pile index
    # prompting user for an input to pick tokens qty to be removed
    tokenQtyToRemove=int(input("How many tokens do you want to remove? "))
    
    while tokenQtyToRemove <=0 or tokenQtyToRemove > pileQty:
        print("Incorrect entry!")
        tokenQtyToRemove=int(input("How many tokens do you want to remove? "))

    # player's pick: pile number and qty of tokens to be removed
    pileIndexAndQty=[]
    pileIndexAndQty.insert(0,chosenPileIndex)
    pileIndexAndQty.insert(1,tokenQtyToRemove) 

    return pileIndexAndQty
   
# the function computes computer's move, random pile pick and qty of tokens
# @param piles
# @param pilesIndices
# returns pileIndexAndQty, the selected pile index and qty of tokens to be removed
def computerMove(piles,pilesIndices):
    # randomly choosing a pile(its index) from piles
    chosenPileIndex=choice(pilesIndices) 
    # randomly choosing tokens qty to be removed
    tokenQtyToRemove=randint(1,piles[chosenPileIndex])
    
    # updating the list pileIndexAndQty with computer's choice
    pileIndexAndQty=[]
    pileIndexAndQty.insert(0,chosenPileIndex)
    pileIndexAndQty.insert(1,tokenQtyToRemove)
        
    return pileIndexAndQty

# the function updates the piles by removing tokens from a selected pile
# @param piles, the list of available token piles
# @param pileIndexAndQty, the selected pile index and qty of tokens to be removed
# returns piles, the updated list of piles
def pilesUpdate(piles, pileIndexAndQty):
    piles[pileIndexAndQty[0]]=piles[pileIndexAndQty[0]]-pileIndexAndQty[1]
    return piles

# the function calculate the total remaining tokens
# @param piles
# returns totalTokens, the total of the remaining tokens
def sumOfTokens(piles):
    totalTokens=sum(piles)
    return totalTokens

########################################## 2. Output functions - printing ##############################################

# The function prints introduciton to the game with basic instruction
def printIntro():
    print()
    print("\n   Welcome to the game of Nim! ")
    print()
    print("<>"*40)
    print("\n  At the begining of the game you will be asked to pick a number of piles and "+
          "\nnumber of tokens for each pile, with which you are going to play. "+
          "\nPlayers are taking turns alternately."+
          "\nWith each turn a player removes a number of tokens from a selected pile. "+
          "\nThe player who removes last token(s) wins. "+
          "\nYou can choose to play against another Player or against Computer. "+
          "\nEnjoy and Good Luck!")
    print()
    print("<>"*40)
          

# the function prints the piles with available tokens
# @param piles, the list of piles
def printPiles(piles):
    print("\nHere are the piles, illustrated below: ")
    for i in range(len(piles)):
        print("pile",i+1,": ","*"* piles[i])

# the function prints a message showing computer's move
# @param pileIndexAndQty - pile index and tokens qty to be removed
def printComputerMove(pileIndexAndQty):
    print()
    print("[]"*5,"Computer removes",pileIndexAndQty[1],"token(s)","from pile",pileIndexAndQty[0]+1,".","[]"*5)

# the function prints a message whose turn it is
# @param currentPlayer
def printWhoseTurn(currentPlayer):
    print("\nIt is %s's turn!" % currentPlayer)

# the function prints a border when the game starts
def printBorderStart():
    print()
    print("*"*29,"%17s" % "The game starts!"," "*2,"*"*29)

# the function prints a border when the game ends
# @param currentPlayer
def printGameOver(currentPlayer):
    print()
    print('"-'*12,'"',end="")
    for e in "The winner is: ":
        print(e, end="")
        sleep(0.1)
    print(currentPlayer,'!!!','"','-"'*12 )
    print()
    print("*"*33," Game over! ","*"*33)

# the function generates a visualized break for Computer "thinking"
def printCompThinking():
    print("Computer is thinking...")
    for i in range(5):
        print(". ", end="")
        sleep(1)
    print()

main()


    
