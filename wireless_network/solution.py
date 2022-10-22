N = int(input())
nodes = set()
connections = set()

for _ in range(N):
    t1, t2, c, h = input().split()

    nodes.add(t1)
    nodes.add(t2)

    connection = [[t1, t2], c, h]
    connection[0].sort()
    connections.add(connection)
