# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        return [int(digit) for digit in str(num)]