class Solution:
    def rob(self, nums) -> int:

        totalA, totalB = 0, 0

        for i in nums:
            temp = max(i + totalA, totalB)
            totalA = totalB
            totalB = temp
        
        return totalB