# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if target <= i:
                count += 1

        return count