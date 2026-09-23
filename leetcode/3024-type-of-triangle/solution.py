# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # check for type of triangle
        def triangleCheck(arrOfSide):
            triangleSet = set(arrOfSide)
            if len(triangleSet) == 2:
                return "isosceles"
            elif len(triangleSet) == 3:
                return "scalene"
            else:
                return "equilateral"
        # Valid triangle check
        if (
            nums[0] + nums[1] > nums[2] and 
            nums[1] + nums[2] > nums[0] and 
            nums[2] + nums[0] > nums[1]): 
            
            return triangleCheck(nums)
            
        return "none"