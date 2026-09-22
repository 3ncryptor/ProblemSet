# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num

        summ = 0

        while num > 0:
            digit = num % 10
            summ += digit 
            num = num // 10

        return self.addDigits(summ)
