class Node():
    '''A class for storing node info'''
    def __init__(self, pos= None, parent= None):
        self.pos = pos  # Position as (row, column) in maze
        self.parent = parent  # Parent node
        self.f = 0 # Sum of g & h
        self.g = 0 # Cost from start to current point
        self.h = 0 # Predicted cost from current point to the end

    def __eq__(self, other):
        '''Compares the possitions'''
        return self.pos == other.pos


def astar(maze, startPos, endPos):
    global N, M, D
    '''Returns a list of tuples as a path from the startPos to the endPos in the maze'''
    openList = []  # Create the open list (σημεια που θα κοιταξει στο αμεσο μέλλον - γειτονικα του closeList)
    closedList = []  # Create the closed list (σημεια που εχει ηδη κοιταξει)

    startNode = Node(startPos) # Define the start node
    endNode = Node(endPos)  # Define the end node

    openList.append(startNode) # Add the start node to the open list

    while len(openList) > 0:  # While the open list is not empty
        # Find the node with the lowest f cost in the open list
        currentNode = openList[0]
        for node in openList:
            if node.f < currentNode.f:
                currentNode = node

        # Remove the current node from the open list and add it to the closed list
        openList.remove(currentNode)
        closedList.append(currentNode)

        # If the current node is the end node return the path that leads to the current node by looking at the parrents
        if currentNode == endNode:
            path = []
            while currentNode.parent is not None:
                path.append(currentNode.pos)
                currentNode = currentNode.parent
            path.append(startNode.pos)
            return True

        # Find all the adjacent valid children to the current node
        children = []
        neighbours = [
            (-1, 0, 0), (0, -1, 0), (0, 1, 0), (1, 0, 0),
            (-1, 0, 1), (0, -1, 1), (0, 1, 1), (1, 0, 1),
            (-1, 0, -1), (0, -1, -1), (0, 1, -1), (1, 0, -1),
        ]

        for addPos in neighbours:
            newPos = (currentNode.pos[0] + addPos[0],
                      currentNode.pos[1] + addPos[1],
                      currentNode.pos[2] + addPos[2])

            # Check if the child is out of bounds
            if newPos[0] not in range(M) or newPos[1] not in range(N) or newPos[2] not in range(D):
                continue

            # Check if the child is a wall
            if maze[newPos[0]][newPos[1]][newPos[2]] == "#":
                continue

            # Add the child to the children list
            children.append(Node(newPos, currentNode))

        # Calculate G, H and F cost for the children
        for child in children:
            # If the child is in the closed list skip it
            if child in closedList:
                continue

            child.g = currentNode.g + 1
            child.h = endNode.pos[0]-child.pos[0]+endNode.pos[1]-child.pos[1]+endNode.pos[2]-child.pos[2]
            child.f = child.g + child.h

            # If the child is already in the open list, but with higher g cost, skip it
            for openNode in openList:
                if child == openNode and child.g >= openNode.g:
                    break

            # Add the child to the open list
            else:
                openList.append(child)

    # If the open list is empty there is no possible path
    return False







T = int(input())

design = []
N = 0
M = 0
D = 0

for _ in range(T):
    N, M, D = list(map(int, input().split()))
    inputIndex = set()
    outputIndex = set()
    for _ in range(D):
        design.append([])
        for _ in range(N):
            design[-1].extend(input().strip().split())
        input()

inlets = []
outlets = []

for i, line in enumerate(design[0]):
    for j, block in enumerate(line):
        if block == "o":
            inlets.append((i,j, 0))

for i, line in enumerate(design[-1]):
    for j, block in enumerate(line):
        if block == "o":
            outlets.append((i,j,D-1))

foundAnswer = False

for start in inlets:
    for end in outlets:
        if astar(design, start, end) == True:
            print("YES")
            foundAnswer = True
            break
if not foundAnswer:
    print("NO")
