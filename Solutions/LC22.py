class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []
        

        def gen(l, r):

            if l == r == n:
                result.append("".join(stack))
                return
            
            if l < n:
                stack.append('(')
                gen(l + 1, r)
                stack.pop()
            
            if r < l:
                stack.append(')')
                gen(l, r + 1)
                stack.pop()

        gen(0, 0)
        return result