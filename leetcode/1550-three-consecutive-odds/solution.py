# Runtime: 4 ms
# Memory: 19.2 MB

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        # oddNumber
        def oddNumber(x):
            if x % 2 != 0:
                return True
        for i in range(0, len(arr)-2):
            if oddNumber(arr[i]) and oddNumber(arr[i+1]) and oddNumber(arr[i+2]):
                return True

        return False

        