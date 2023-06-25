triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

for row in triangle[::-1]:
    for i, n in enumerate(row):
        print(i, n)
