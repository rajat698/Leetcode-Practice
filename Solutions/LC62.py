m = 7
n = 3

grid = [[0] * (n)] * (m - 1)
x = [1] * n

grid.append(x)

for i in range(len(grid)):
    grid[i][n-1] = 1

for i in range(len(grid) - 2, -1, -1):
    for j in range(len(grid[0]) -2, -1, -1):
        grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

print(grid)