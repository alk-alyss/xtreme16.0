def getSolution(l, r, k, p):
    global array


n, m, p = list(map(int, input().split()))

array = [0 for _ in range(n + 1)]

rules = []
indexes = set()
for _ in range(m):
    rules.append(list(map(int, input().split())))
    for i in range(rules[-1][0], rules[-1][1] + 1):
        if i not in indexes:
            array[i] = rules[-1][2]
            break
    else:
        print('None')
    indexes.add(tuple(range(rules[-1][0], rules[-1][1] + 1)))

array.pop()
output = ""
for number in array:
    number = str(number)
    output += number + " "
output = output[:-1]
print(output)
