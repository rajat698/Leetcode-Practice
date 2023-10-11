class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split('/')
        stack = []

        for i in path:
            if stack and i == '..':
                stack.pop()

            elif i == '.' or i == '' or i == '..':
                continue

            else:
                stack.append(i)
        
        result_string = "/"

        for i in stack:
            result_string = result_string + i + "/"
        
        return result_string if len(result_string) == 1 else result_string[0:len(result_string) - 1]