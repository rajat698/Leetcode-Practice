class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        distance = [[float("inf")] * (len(grid[0]) + 1)] * (len(grid) + 1)

        distance[len(distance) - 1][len(distance[0]) - 2] = 0

        for rows in range(len(grid) - 1, -1, -1):
            for cols in range(len(grid[0]) - 1, - 1, -1):

                distance[rows][cols] = grid[rows][cols] + min(distance[rows + 1][cols], distance[rows][cols + 1])
        
        return distance[0][0]