class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m + n - 1
        while m > 0 and n > 0:

            if nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            
            else:
                nums1[i] = nums2[n - 1]
                n -= 1
            
            i -= 1

        for j in range(n):
            nums1[j] = nums2[j]