class Solution:
    def majorityElement(self, nums) -> int:
        counter = {}

        for i in nums:
            if i not in counter:
                counter[i] = 1

            else:
                counter[i] += 1

        maximum = max(counter.values())

        for i in counter.keys():
            if counter[i] == maximum:

                return i