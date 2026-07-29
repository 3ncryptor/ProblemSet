# Runtime: 7 ms
# Memory: 19.5 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        def helper(ind, target):
            if ind == len(candidates):
                if target == 0:
                    res.append(sol[:])
                return

            # not pick
            helper(ind + 1, target)

            # pick
            if candidates[ind] <= target:
                sol.append(candidates[ind])
                helper(ind, target - candidates[ind])
                sol.pop()

            return res

        result = helper(0, target)
        return result