class Solution:
    def reverseWords(self, s: str) -> str:

        def createList(s):
            newList = []

            l, r = 0, 0

            while r < len(s):

                if s[l] == ' ':
                    l += 1
                    r += 1
                    continue
                
                if s[r] == ' ':
                    newList.append(s[l:r])
                    l = r + 1
                    r += 1
                
                elif r == len(s) - 1:
                    newList.append(s[l:r + 1])
                    l = r + 1
                    r += 2

                else:
                    r += 1

            
            return newList

        newList = createList(s)
        result = ""

        r = len(newList) - 1

        while r > 0:

            result = result + newList[r] + ' '
            r -= 1
        
        result = result + newList[0]


        return result