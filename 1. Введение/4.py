index = 0
# L = [1, 4, 67, 4, 2, 65, 66]
# L = [1, 2, 6]
L = [1, 2]
for i in range(len(L)):
    if i == len(L) - 1:
        break
    if L[i + 1] - L[i] == 1:
        index = i
print(index)