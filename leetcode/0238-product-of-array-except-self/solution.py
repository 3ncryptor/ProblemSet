# Runtime: 19 ms
# Memory: 25.2 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        result = []
        
        for i in nums:
            result.append(prefix)
            prefix *= i

        # print(result)
        
        for i in range(len(nums) - 1, -1, -1):
            # print(result[i], nums[i], i, suffix)
            result[i] *= suffix
            suffix *= nums[i]
            # print(result[i], nums[i], i, suffix)

        # print(result)
        
        return result