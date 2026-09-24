# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleDigitSum = 0
        doubleDigitSum = 0
        for i in nums:
            if i >= 10:
                doubleDigitSum += i
            else:
                singleDigitSum += i

        return True if singleDigitSum > doubleDigitSum else True if singleDigitSum < doubleDigitSum else False
    