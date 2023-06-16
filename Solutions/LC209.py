class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minimal = 99999999999999
        l, r = 0, 0
        sum = 0
        

        while r < len(nums):
            if sum + nums[r] < target:
                sum = sum + nums[r]
                r += 1
            
            else:
                minimal = min(minimal, r - l + 1)
                sum -= nums[l]
                l += 1
        
        return minimal if minimal != 99999999999999 else 0