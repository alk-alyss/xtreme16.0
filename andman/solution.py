from functools import cache

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

def DFS(node, end):
    path = [node]

    if node == end:
        return path

    if node.children == []:
        return None

    for connection in node.children:
        nextPath = DFS(connection, end)
        if nextPath == None:
            continue
        else:
            path.extend(nextPath)

    if len(path) > 1:
        return path
    else:
        return None

def findAnswer(n1, n2):
    answer = 1
    start = n1
    end = n2

    path = []
    while True:
        nextPath = DFS(start, end)
        if nextPath != None:
            path.extend(nextPath)
            break

        path.append(start)

        if start.parent == None:
            break
        start = start.parent

    for node in path:
        answer *= node.weight

    return answer%1000000007

from collections import defaultdict

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

        nodes[u].addChild(nodes[v])
        nodes[v].addParent(nodes[u])

    Q = int(input())

    for _ in range(Q):
        t, u, v = list(map(int, input().split()))

        if t == 1:
            u -= 1
            nodes[u].weight = v

        elif t == 2:
            u -= 1
            v -= 1
            output.append(findAnswer(nodes[u], nodes[v]))

    for o in output:
        print(o)
