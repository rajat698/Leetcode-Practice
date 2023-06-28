class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        baseRow = [1] * n

        for i in range(m - 2, -1, -1):
            NewRow = [1] * n
            for j in range(n - 2, -1, -1):
                NewRow[j] = baseRow[j] + NewRow[j + 1]
            
            baseRow = NewRow

        return baseRow[0]