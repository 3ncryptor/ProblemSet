# Runtime: 2 ms
# Memory: 19.6 MB

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        length = len(nums1)
        mid = length // 2

        if length % 2 != 0:
            return float(nums1[mid])
        else:
            return (nums1[mid - 1] + nums1[mid]) / 2.0