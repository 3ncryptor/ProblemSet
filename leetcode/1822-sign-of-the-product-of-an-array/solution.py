# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        prod = 1
        for i in nums:
            prod *= i

        def signFunc(x):
            return 1 if x > 0 else -1 if x < 0 else 0

        return signFunc(prod)
        