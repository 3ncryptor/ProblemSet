# Runtime: 70 ms
# Memory: 29.6 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            w = right - left
            h = min(height[left],height[right])
            a = w * h

            max_area = max(max_area, a)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
            