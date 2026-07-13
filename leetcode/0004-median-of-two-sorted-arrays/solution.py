# Runtime: 0 ms
# Memory: 19.6 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 1:
            return nums1[length // 2]
        else:
            mid1, mid2 = nums1[length // 2 - 1], nums1[length // 2]
            return (mid1 + mid2) / 2.0