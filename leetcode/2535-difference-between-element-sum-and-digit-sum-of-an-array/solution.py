# Runtime: 11 ms
# Memory: 19.5 MB

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        normalSum = 0
        for i in nums:
            normalSum += i

        digitWiseSum = 0
        for i in nums:
            while i > 0:
                digit = i % 10
                i //= 10
                digitWiseSum += digit

        return abs(normalSum - digitWiseSum)
            
        