#LC200. Number of Islands

import collections

class Solution:
    def numIslands(self, grid) -> int:
        
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        count = 0
        visited = set()
        
        def bfs(i, j):
            
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            
            while q:
                r, c = q.pop()
                
                for x, y in directions:
                    if ((r + x) in range(row)) and ((c + y) in range(col)) and grid[r + x][c + y] == "1" and (r+x, c+y) not in visited:
                        q.append((r+x, c+y))
                        visited.add((r+x, c+y))
                        
        for i in range(row):
            for j in range(col):

                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    count += 1

        return count