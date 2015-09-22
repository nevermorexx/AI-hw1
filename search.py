import pegSolitaireUtils
import config
import stack

def ItrDeepSearch(pegSolitaireObject):
    #################################################
    # Must use functions:
    # getNextState(self,oldPos, direction)
    #
    # we are using this function to count,
    # number of nodes expanded, If you'll not
    # use this grading will automatically turned to 0
    #################################################
    #
    # using other utility functions from pegSolitaireUtility.py
    # is not necessary but they can reduce your work if you
    # use them.
    # In this function you'll start from initial gameState
    # and will keep searching and expanding tree until you
    # reach goal using Iterative Deepning Search.
    # you must save the trace of the execution in pegSolitaireObject.trace
    # SEE example in the PDF to see what to save
    #
    #################################################

    directionSets = config.DIRECTION.values()
    myStack = stack.Stack()

    #initial the stack with first one-depth search
    for row in range(7):
        for col in range(7):
            if pegSolitaireObject.gameState[row][col] == 1:
                oldPos = (row, col)
                for direction in directionSets:
                    if pegSolitaireObject.is_validMove(oldPos, direction):
                        myStack.push(oldPos)
                        myStack.push(direction)

    while (not pegSolitaireObject.reachDestination()):
        if (not myStack.isEmpty()):
            myDirection = myStack.pop()    #make a move
            myPos = myStack.pop()
            oldStackSize = myStack.size()
            pegSolitaireObject.getNextState(myPos, myDirection)
            if pegSolitaireObject.reachDestination():
                return True
            else:
                for row in range(7):
                    for col in range(7):
                        if pegSolitaireObject.gameState[row][col] == 1:
                            oldPos = (row, col)
                            for direction in directionSets:
                                if pegSolitaireObject.is_validMove(oldPos, direction):
                                    myStack.push(oldPos)
                                    myStack.push(direction)
                newStackSize = myStack.size()
                if newStackSize == oldStackSize: #reach a dead end, we need to trace back
                    pegSolitaireObject.traceBack()
        else:
            print "no solution for this map"
            return False

    return True


def aStarOne(pegSolitaireObject):
    #################################################
    # Must use functions:
    # getNextState(self,oldPos, direction)
    #
    # we are using this function to count,
    # number of nodes expanded, If you'll not
    # use this grading will automatically turned to 0
    #################################################
    #
    # using other utility functions from pegSolitaireUtility.py
    # is not necessary but they can reduce your work if you
    # use them.
    # In this function you'll start from initial gameState
    # and will keep searching and expanding tree until you
    # reach goal using A-Star searching with first Heuristic
    # you used.
    # you must save the trace of the execution in pegSolitaireObject.trace
    # SEE example in the PDF to see what to return
    #
    #################################################
    return True


def aStarTwo(pegSolitaireObject):
    #################################################
    # Must use functions:
    # getNextState(self,oldPos, direction)
    #
    # we are using this function to count,
    # number of nodes expanded, If you'll not
    # use this grading will automatically turned to 0
    #################################################
    #
    # using other utility functions from pegSolitaireUtility.py
    # is not necessary but they can reduce your work if you
    # use them.
    # In this function you'll start from initial gameState
    # and will keep searching and expanding tree until you
    # reach goal using A-Star searching with second Heuristic
    # you used.
    # you must save the trace of the execution in pegSolitaireObject.trace
    # SEE example in the PDF to see what to return
    #
    #################################################
    return True
