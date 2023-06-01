#2Sum II
class Solution:
    def twoSum(self, numbers, target: int):

        l, r = 0, len(numbers) - 1

        while l < r:

            twoSum = numbers[l] + numbers[r]

            if twoSum > target:
                r -= 1
            
            elif twoSum < target:
                l += 1
            
            else:
                return [l + 1, r + 1]