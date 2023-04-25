class Solution:
    def findRepeatedDnaSequences(self, s: str):

        result, temp = set(), set()

        for i in range(len(s) - 9):

            if s[i:i + 10] not in temp:
                temp.add(s[i:i + 10])
            
            else:
                result.add(s[i:i + 10])

        return result