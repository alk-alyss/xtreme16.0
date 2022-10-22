from collections import defaultdict


class INode:
    def __init__(self, id, character, yes_id, no_id) -> None:
        self.id = id
        self.character = character
        self.yes_id = yes_id
        self.no_id = no_id


class LNode:
    def __init__(self, id, language) -> None:
        self.id = id
        self.language = language


tree = defaultdict(list)
n, p = map(int, list(input().split()))
characters = set()

for _ in range(n):
    node = input().split()
    if node[0] == 'I':
        temp = INode(node[1], node[2], node[3], node[4])
        characters.add(node[2])
        tree[node[2]].append(temp)
    else:
        temp = LNode(node[1], node[2])
        tree[node[1]].append(temp)

answer = []
for _ in range(p):
    phrase = input()
    phrase = set(phrase)
    print(phrase)
# print(phrase)
