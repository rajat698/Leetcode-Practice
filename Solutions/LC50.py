class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):

            if x == 0:
                return 0
            if n == 0:
                return 1

            answer = helper(x, n//2)
            answer = answer * answer
            return answer * x if n % 2 else answer

        result = helper(x, abs(n))
        return result if n > 0 else 1/result