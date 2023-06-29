class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        baseRow = [0] * len(obstacleGrid[0])
        baseRow[len(obstacleGrid[0]) - 1] = 1

        for i in reversed(range(len(obstacleGrid))):
            for j in reversed(range(len(obstacleGrid[0]))):
                if obstacleGrid[i][j]:
                    baseRow[j] = 0
                elif j + 1 < len(obstacleGrid[0]):
                    baseRow[j] = baseRow[j] + baseRow[j + 1]
        
        return baseRow[0]