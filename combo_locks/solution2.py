from collections import OrderedDict as od

word_length = [0 for _ in range(8)]
words = [[] for _ in range(8)]
wheels = [[{} for _ in range(8)] for _ in range(8)]
with open('words.txt', "r") as file:
    for row in file:
        # print(len(row.strip()))
        length = len(row.strip())
        word_length[length - 1] += 1
        words[length - 1].append(row.strip())
    # print(words)

for i in range(8):
    # iterating through the length of the words
    # print(words[i])
    for j, word in enumerate(words[i]):
        # we get in v the many words
        # print(v)
        for pos, letter in enumerate(word):
            # print(letter)
            # we get the wheels for the specific wheel set letters
            if letter not in wheels[i][pos].keys():
                wheels[i][pos][letter] = 1
            else:
                wheels[i][pos][letter] += 1

# for i in range(8):
#     # print(i, '\n------------------')
#     # length of words
#     for j in range(i):
#         # each wheel for the length of words
#         # wheels[i][j] = sorted(wheels[i][j].items(), key=lambda item: item[1], reverse=True)
#         # print(wheels[i][j], '\n')
#         pass


for j in range(8):
    wheels[7][j] = sorted(wheels[7][j].items(), key=lambda item: item[1], reverse=True)

# print(wheels[7])
# list(dict.fromkeys(keywords))
sets = [{} for _ in range(8)]
output = ''

for i in range(8):
    ind = 0
    while len(list(dict.fromkeys(sets[i]))) < 10:
        # sets[i].add(wheels[7][i][ind][0])
        sets[i][wheels[7][i][ind][0]] = 0
        ind += 1
    # print(sets[i])

output = ''
for i in range(8):
    output += ''.join(list(dict.fromkeys(sets[i])))+'\n'
    # print(wheels[7][i])
    # output += ''.join([wheels[7][i][item][0] for item in range(10)]) + '\n'
print(output)

ans = """csparemdbt
eoarinulht
ratensomic
eiatronpls
itrenalosc
iaentorslc
enratolics
sedgynrtla"""

# print(word_length)
# for letter in alphabet:
#     print(f"{letter}: {alphabet[letter]}")
#
# wheels = [[] for _ in range(8)]
#
# for i in range(8):
#     letters = []
#     for letter in alphabet:
#         letters.append((alphabet[letter][i], letter))
#     letters = sorted(letters, key=lambda x: x[0], reverse=True)
#     wheels[i] = letters[:10]
#
# for i, wheel in enumerate(wheels):
#     row = ""
#     if i > 1:
#         for letter in wheel[:-1]:
#             row += letter[1]
#     else:
#         for letter in wheel:
#             row += letter[1]
#     print(row)
# print()
# ##################
# ans = """scpabmtrdf
# aeoirulhnt
# ranteilso
# eitanlsrd
# eistrnalo
# ensritadl
# esntrgdal
# sedgynrtl"""
#
# print(ans)
