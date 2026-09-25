# Runtime: 19 ms
# Memory: 19.2 MB

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        currentPos = [0,0]
        # UD changes the y axis
        # RL changes the x axis
        # (0,0) ==> (xaxis, yaxis)

        for i in moves:
            if (i == "U"):
                currentPos[1] += 1
            elif i == "D":
                currentPos[1] -= 1
            elif i == "L":
                currentPos[0] -= 1
            elif i == "R":
                currentPos[0] += 1

        return True if currentPos == [0,0] else False
        