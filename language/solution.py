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

def inorder(node):
    global tree, langIds, disabledIds

    output = []

    if node.id in disabledIds:
        return output

    if node.id in langIds:
        output.append(node.language)
    else:
        output.extend(inorder(tree[node.yes_id][0]))

        output.extend(inorder(tree[node.no_id][0]))

    return output


tree = defaultdict(list)
n, p = list(map(int, input().split()))
characters = set()
root = None
charToId = {}
langIds = set()
connections = set()

for _ in range(n):
    node = input().split()
    if node[0] == 'I':
        temp = INode(node[1], node[2], node[3], node[4])
        characters.add(node[2])
        tree[node[1]].append(temp)
        charToId[node[2]] = node[1]
        connections.add(node[3])
        connections.add(node[4])
        if node[1] not in connections: root = node[1]
    else:
        temp = LNode(node[1], node[2])
        tree[node[1]].append(temp)
        langIds.add(node[1])

for _ in range(p):
    disabledIds = []
    phrase = set(input()).intersection(characters)

    for char in phrase:
        disabledIds.append(tree[charToId[char]][0].no_id)

    output = inorder(tree[root][0])
    output.sort()
    output = ' '.join(output)

    print(output)
