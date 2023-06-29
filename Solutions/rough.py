obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

for i in range(len(obstacleGrid[len(obstacleGrid) - 1])):
    if obstacleGrid[len(obstacleGrid) - 1][i] == 1:
        obstacleGrid[len(obstacleGrid) - 1][i] = 0
    else:
        obstacleGrid[len(obstacleGrid) - 1][i] = 1

print(obstacleGrid)