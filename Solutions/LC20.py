class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {')':'(', '}':'{', ']':'['}

        stack = []

        for i in s:

            if i in "([{":
                stack.append(i)
            
            elif stack and i in ')]}':

                n = stack.pop()

                if n == brackets[i]:
                    continue

                else:
                    return False

            else:
                return False

        return True if not stack else False                