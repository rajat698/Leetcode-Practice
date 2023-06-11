class Solution:
    def longestConsecutive(self, nums) -> int:

        numSet = set(nums)

        result = 0

        for i in numSet:
            if i - 1 not in numSet:
                count = 1
                while i + count in numSet:
                    count += 1
                
                result = max(result, count)

        return result