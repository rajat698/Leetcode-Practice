class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        newSet = set()

        l = 0
        result = 0

        for r in range(len(s)):

            while s[r] in newSet:
                newSet.remove(s[l])
                l += 1

            newSet.add(s[r])
            result = max(result, r - l + 1)

        return result