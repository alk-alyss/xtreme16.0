alphabet = {}

for letter in range(ord('a'), ord('z') + 1):
    alphabet[chr(letter)] = [0 for _ in range(8)]

words = [0 for _ in range(8)]
with open('combo_locks/words.txt', "r") as file:
    for row in file:
        # print(len(row.strip()))
        words[len(row.strip())-1] += 1
        for i, letter in enumerate(row.strip()):
            alphabet[letter][i] += 1
print(words)
for letter in alphabet:
    print(f"{letter}: {alphabet[letter]}")

wheels = [[] for _ in range(8)]

for i in range(8):
    letters = []
    for letter in alphabet:
        letters.append((alphabet[letter][i], letter))
    letters = sorted(letters, key=lambda x: x[0], reverse=True)
    wheels[i] = letters[:10]

for i, wheel in enumerate(wheels):
    row = ""
    if i > 3:
        for letter in wheel[:-1]:
            row += letter[1]
    else:
        for letter in wheel:
            row += letter[1]
    print(row)
print()
##################
ans = """scpabmtrdf
aeoirulhnt
ranteilsoc
eitanlsrdo
eistrnalo
ensritadl
esntrgdal
sedgynrtl"""

print(ans)
