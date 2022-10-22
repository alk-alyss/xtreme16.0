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

def findLangs(phrase, node):
    global tree

    currentNode = node
    output = []

    if isinstance(currentNode, LNode):
        output.append(currentNode.language)
        return output

    nextNodeId = currentNode.yes_id
    nextNode = tree[nextNodeId]
    output.extend(findLangs(phrase, nextNode))

    if node.character not in phrase:
        nextNodeId = currentNode.no_id
        nextNode = tree[nextNodeId]
        output.extend(findLangs(phrase, nextNode))

    return output


tree = {}
n, p = list(map(int, input().split()))
characters = set()
root = None
charToId = {}
connections = set()

for _ in range(n):
    s = input().split()
    nodeId = s[1]

    if s[0] == 'I':
        char = s[2]
        yesId = s[3]
        noId = s[4]

        node = INode(nodeId, char, yesId, noId)

        characters.add(char)
        charToId[char] = nodeId

        connections.add(yesId)
        connections.add(noId)

    else:
        lang = s[2]

        node = LNode(nodeId, lang)

    tree[nodeId] = node

for nodeId in tree.keys():
    if nodeId not in connections: root = nodeId

for _ in range(p):
    phrase = set(input()).intersection(characters)

    result = findLangs(phrase, tree[root])
    result.sort()
    print(' '.join(result))
