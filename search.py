import pegSolitaireUtils
import config
import stack
import heapq

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

    depth = 0
    is_solvable = True

    oldTotolExpandedNodes = [0]
    #getNextState function is used in the my_IDS function
    #is_solvable is used when the game has no solution, and can avoid infinite loop
    while (not pegSolitaireObject.reachDestination()):
        depth += 1
        oldTotolExpandedNodes.append(my_IDS(pegSolitaireObject,depth))
        lenth = len(oldTotolExpandedNodes)
        if oldTotolExpandedNodes[lenth-1] == oldTotolExpandedNodes[lenth-2]:
        #calculate the nodesExpanded count, if 2 different levels have the same count but didn't reach
        #the goal, indicating that this map has no solution
            break

    if (not pegSolitaireObject.reachDestination()):
        print "No solution for this map"

    return True

def my_IDS(pegSolitaireObject,depth):
    directionSets = config.DIRECTION.values()
    myStack = stack.Stack()
    fense = (-1,-1)

    currentDepthNodesExpanded = 0 #this variable is used to count the total number of expanded nodes

    #depth1 stack, search for all possible nodes, push them in the stack
    for row in range(7):
        for col in range(7):
            if pegSolitaireObject.gameState[row][col] == 1:
                oldPos = (row, col)
                for direction in directionSets:
                    if pegSolitaireObject.is_validMove(oldPos, direction):
                        myStack.push(direction)
                        myStack.push(oldPos)
    currentDepth = 1

    myStack.push(fense)
    #fense is used to seperate different depths of nodes, if one depth of nodes are all poped, we need to
    #check for the next node in the lower depth. when 2 fenses meet, it shows that the higher depth of nodes
    #are all searched.

    while (myStack.size() > 1):
        currentFence = myStack.pop()
        oldPos = myStack.pop()
        while (oldPos[0] == -1):
            print "i reached here"
            print "TRACE :"
            if myStack.isEmpty():  #checked all cases
                pegSolitaireObject.traceBack()
                return currentDepthNodesExpanded
            currentDepth -= 1
            oldPos = myStack.pop()
            pegSolitaireObject.traceBack()
            for row in pegSolitaireObject.gameState:
                print row
        oldDir = myStack.pop()
        pegSolitaireObject.getNextState(oldPos,oldDir)
        currentDepthNodesExpanded += 1
        print "move %d,%d by %d,%d" %(oldPos[0],oldPos[1],oldDir[0],oldDir[1])
        myStack.push(currentFence)

        if pegSolitaireObject.reachDestination():
            return currentDepthNodesExpanded
        else:
            if currentDepth < depth:
                for row in range(7):
                    for col in range(7):
                        if pegSolitaireObject.gameState[row][col] == 1:
                            oldPos = (row, col)
                            for direction in directionSets:
                                if pegSolitaireObject.is_validMove(oldPos, direction):
                                    myStack.push(direction)
                                    myStack.push(oldPos)
                myStack.push(currentFence)
                currentDepth += 1
            else:
                print "BEFORE TRACE BACK"
                print pegSolitaireObject.trace
                for row in pegSolitaireObject.gameState:
                    print row
                pegSolitaireObject.traceBack()
                print "AFTER TRACE BACK"
                print pegSolitaireObject.trace
                for row in pegSolitaireObject.gameState:
                    print row

    return currentDepthNodesExpanded



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

    #################################################
    #The algorithm for aStarOne is to assign each cell with different values: the closer to the goal cell,
    #the smaller value it has. For all expanded nodes, we calculate the total value of the gameState
    #for each subnode. Use a heap to store all the expanded nodes, use the total value we calculated as the key.
    #Push the nodes with lager values first, because there are relatively more nodes far away from the center.
    #Nodes with smaller values get pushed later, so they can be checked earlier to improve the performance.
    
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
