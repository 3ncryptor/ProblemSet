# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []

        while len(nums) > 0:
            # Alice's Turn
            alicePop = nums.pop(0)
            # Bob's Turn
            bobPop = nums.pop(0)
            # append to arr
            arr.extend([bobPop, alicePop])
        
        return arr
        