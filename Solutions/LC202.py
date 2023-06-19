class Solution:

    def isHappy(self, n: int) -> bool:

        visited = set()

        while n not in visited:
            visited.add(n)
            curr = self.helper(n)

            if curr == 1:
                return True

            n = curr
        
        return False

    def helper(self, n):
        summ = 0

        while n:
            curr = n % 10
            summ += curr ** 2
            n = n // 10
        
        return summ