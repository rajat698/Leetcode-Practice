#15. 3Sum

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        lis = []
        for i in range(len(nums)):

            l,r = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    lis.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return lis