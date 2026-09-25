# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxx = 0

        for i in sentences:
            words = i.split()
            maxx = max(maxx, len(words))

        return maxx

        