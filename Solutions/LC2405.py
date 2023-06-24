class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        letters = set()

        for i in s:
            if i not in letters:
                letters.add(i)
            
            else:
                count += 1
                letters = set()
                letters.add(i)

        return count