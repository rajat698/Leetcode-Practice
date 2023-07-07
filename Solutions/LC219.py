class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dictionary = {}

        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = i
            
            else:
                if abs(dictionary[nums[i]] - i) <=k:
                    return True
                else:
                    dictionary[nums[i]] = i
        
        return False