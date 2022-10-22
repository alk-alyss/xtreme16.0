from collections import defaultdict


class Node:
    def __init__(self, weight):
        self.weight = weight
        self.parent = None
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def addParent(self, node):
        self.parent = node

    def __str__(self):
        return str(self.weight)


def findAnswer(path, nodes):
    answer = 1

    for node in path:
        answer *= nodes[node].weight

    return answer % 1000000007


route = []


def DFS(vis, x, y, stack):
    global route
    stack.append(x)
    if (x == y):

        # print the path and return on
        # reaching the destination node
        route = stack.copy()
        return
    vis[x] = True

    # if backtracking is taking place

    if (len(connections[x]) > 0):
        for j in connections[x]:

            # if the node is not visited
            if (vis[j] == False):
                DFS(vis, j, y, stack)

    del stack[-1]

# A utility function to initialise
# visited for the node and call
# DFS function for a given vertex x.


def DFSCall(x, y, n, stack):

    # visited array
    vis = [0 for i in range(n + 1)]

    #memset(vis, false, sizeof(vis))

    # DFS function call
    DFS(vis, x, y, stack)


T = int(input())

for _ in range(T):
    N = int(input())
    output = []

    nodes = [Node(weight) for weight in list(map(int, input().split()))]
    connections = defaultdict(list)

    for n in range(N-1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        connections[u].append(v)
        connections[v].append(u)

    print(connections)

    Q = int(input())

    # for _ in range(Q):
    #     t, u, v = list(map(int, input().split()))

    #     if t == 1:
    #         u -= 1
    #         nodes[u].weight = v

    #     elif t == 2:
    #         u -= 1
    #         v -= 1
    #         DFSCall(u, v, N, [])
    #         output.append(findAnswer(route, nodes))

    # for o in output:
    #     print(o)
