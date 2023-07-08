class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(0.1)
        l, r = 0, 1
        result = []

        while r < len(nums):

            curr = ""
            curr += str(nums[l])

            while r < len(nums) and nums[r] - nums[r - 1] == 1:
                curr = str(nums[l]) + "->" + str(nums[r])
                r += 1

            l = r
            r += 1

            result.append(curr)
            
        return result