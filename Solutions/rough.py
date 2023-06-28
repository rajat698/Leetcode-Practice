m = 3
n = 7

baseRow = [1] * n

for i in range(m - 2, -1, -1):
    NewRow = [1] * n
    for j in range(n - 2, -1, -1):
        NewRow[j] = baseRow[j] + NewRow[j + 1]
    
    baseRow = NewRow

print(baseRow[0])