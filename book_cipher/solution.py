def cleanXML(xml):
    output = ""
    getOutput = False
    for char in xml:
        if char == ">":
            getOutput = True
        elif char == "<":
            getOutput = False
        elif getOutput:
            output += char

    return output

def generateCipher(text, row, col):
    cipher = []
    for r in range(row):
        start = r*col
        end = (r+1)*col

        try:
            newRow = text[start:end]
        except IndexError:
            newRow = text[start:-1]
        cipher.append(newRow)

    return cipher

from collections import defaultdict
def generateDictionary(cipher, reverse=False):
    d = defaultdict(list)

    if reverse:
        cipher.reverse()

    for i, row in enumerate(cipher):
        if reverse:
            row.reverse()

        for j, char in enumerate(row):
            if char not in d:
                d[char] = [i+1, j+1]

    return d

def encode(text, dictionary):
    encoded = []
    for char in text:
        if char not in dictionary:
            return None
        encoded.extend(dictionary[char])

    return encoded

p = int(input())
n = int(input())
r, c = list(map(int, input().split(',')))
largest = True if input() == "L" else False

phrases = []
for _ in range(p):
    phrases.append(input())

xml = ""
for _ in range(n):
    xml += input()

cleanxml = cleanXML(xml)
cipher = generateCipher(cleanxml, r, c)
cipherDictionary = generateDictionary(cipher, largest)

for phrase in phrases:
    encodedPhrase = encode(phrase, cipherDictionary)

    if encodedPhrase == None:
        print(0)
        continue

    output = ','.join(list(map(str,encodedPhrase)))
    print(output)
