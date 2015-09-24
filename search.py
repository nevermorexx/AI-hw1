import pegSolitaireUtils
import config
import stack
import heapq
import copy

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
    oldTotolExpandedNodes = [0]
    #this list is used to store the count of expanded nodes at different depths

    #getNextState function is used in the my_IDS function
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
        while (oldPos[0] == -1):   #in the while loop, indicating higher depth nodes are all checked
            if myStack.isEmpty():  #checked all cases
                pegSolitaireObject.traceBack()
                return currentDepthNodesExpanded
            currentDepth -= 1
            oldPos = myStack.pop()
            pegSolitaireObject.traceBack()
        oldDir = myStack.pop()
        pegSolitaireObject.getNextState(oldPos,oldDir)
        currentDepthNodesExpanded += 1
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
                pegSolitaireObject.traceBack()

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

    #This algorithm counts the number of isolated nodes(i.e. a node wholse N.W.E.S. four directions neibours
    # are not pegs.H(n) = #isolated nodes. we use heap to store the pegSolitaireObject for each nodes and the
    # number as the key. We always expand the node in the heap with least number of isolated
    # nodes(i.e. with least value). We keep searching until we find the goal. If the heap becomes empty
    # and the goal is not fount, the map has no solution.

    directionSets = config.DIRECTION.values()
    myHeap = []

    #init the heap with first depth expanded nodes
    for row in range(7):
        for col in range(7):
            if pegSolitaireObject.gameState[row][col] == 1:
                oldPos = (row, col)
                for direction in directionSets:
                    if pegSolitaireObject.is_validMove(oldPos, direction):
                        pegSolitaireObject.getNextState(oldPos,direction)

                        if pegSolitaireObject.reachDestination():
                            return True
                        newPegObj = copy.deepcopy(pegSolitaireObject)
                        heapq.heappush(myHeap,(getIsolatedNodesCount(newPegObj),newPegObj))
                        pegSolitaireObject.traceBack()

    while (len(myHeap) != 0):   #pop the node with min value and expand that node, add new nodes to the heap
        currentNode = heapq.heappop(myHeap)
        currentPegObj = copy.deepcopy(currentNode[1])

        for i in range(7):
            for j in range(7):
                if currentPegObj.gameState[i][j] == 1:
                    oldPos = (i, j)
                    for direction in directionSets:
                        if currentPegObj.is_validMove(oldPos,direction):
                            currentPegObj.getNextState(oldPos,direction)
                            pegSolitaireObject.nodesExpanded += 1
                            # because here we move the copy of pegSolitaireObject, so the total nodesExpanded
                            # should be added by one in pegSolitaireObject
                            if currentPegObj.reachDestination():
                                pegSolitaireObject.trace = copy.deepcopy(currentPegObj.trace)
                                # similar as above, we moved the copy of the pegSolitaireObject, so
                                # we need to copy back the final trace
                                return True
                            newPegObj = copy.deepcopy(currentPegObj)
                            heapq.heappush(myHeap,(getIsolatedNodesCount(newPegObj),newPegObj))
                            currentPegObj.traceBack()
    if (len(myHeap) == 0):
        print "No solution for this map"

    return True

def getIsolatedNodesCount(pegSolitaireObject):

    directionSets = config.DIRECTION.values()
    count = 0
    for row in range(7):
        for col in range(7):
            if pegSolitaireObject.gameState[row][col] == 1:
                oldPos = (row, col)
                directionCount = 0
                for directionIndex in range(4):
                    direction = directionSets[directionIndex]
                    r1 = oldPos[0] + direction[0]
                    c1 = oldPos[1] + direction[1]
                    if r1 < 0 or r1 > 6 or c1 < 0 or c1 > 6:
                        directionCount += 1
                        continue
                    else:
                        if pegSolitaireObject.gameState[r1][c1] != 0:
                            break
                        else:
                            directionCount += 1

                if directionCount == 4:
                    count += 1
    return count


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
    ################################################

    #################################################
    #The algorithm for aStarOne is to assign each cell with different values: the closer to the goal cell,
    # the smaller value it has. For all expanded nodes, we calculate the total value of the gameState
    # for each subnode. value(cell) = abs(x-3) + abs(y-3), H(n) = total value of the gameState.
    # Use a heap to store all the expanded nodes, use the total value we calculated as the key.
    # Then sort the heap. Nodes with smaller values get poped from the heap earlier, so they can be
    # checked from the stack earlier to improve the performance.
    # If the heap becomes empty and the goal is not fount, the map has no solution.
    directionSets = config.DIRECTION.values()
    myHeap = []

    #init the heap with first depth expanded nodes
    for row in range(7):
        for col in range(7):
            if pegSolitaireObject.gameState[row][col] == 1:
                oldPos = (row, col)
                for direction in directionSets:
                    if pegSolitaireObject.is_validMove(oldPos, direction):
                        pegSolitaireObject.getNextState(oldPos,direction)
                        if pegSolitaireObject.reachDestination():
                            return True
                        newPegObj = copy.deepcopy(pegSolitaireObject)
                        heapq.heappush(myHeap,(getTotalValue(newPegObj),newPegObj))
                        pegSolitaireObject.traceBack()

    while (len(myHeap) != 0):   #pop the node with min value and expand that node, add new nodes to the heap
        currentNode = heapq.heappop(myHeap)
        currentPegObj = copy.deepcopy(currentNode[1])

        for i in range(7):
            for j in range(7):
                if currentPegObj.gameState[i][j] == 1:
                    oldPos = (i, j)
                    for direction in directionSets:
                        if currentPegObj.is_validMove(oldPos,direction):
                            currentPegObj.getNextState(oldPos,direction)
                            pegSolitaireObject.nodesExpanded += 1
                            if currentPegObj.reachDestination():
                                pegSolitaireObject.trace = copy.deepcopy(currentPegObj.trace)
                                return True
                            newPegObj = copy.deepcopy(currentPegObj)
                            heapq.heappush(myHeap,(getTotalValue(newPegObj),newPegObj))
                            currentPegObj.traceBack()
    if (len(myHeap) == 0):
        print "No solution for this map"
    return True

#get total value of the gameState
def getTotalValue(pegSolitaireObject):
    totalValue = 0
    for i in range(7):
        for j in range(7):
            if pegSolitaireObject.gameState[i][j] == 1:
                totalValue += getCellValue(i,j)

    return totalValue

#use the manhatton function to assign each cell with a peg a value
def getCellValue(row, col):
    return abs(row-3)+abs(col-3)
