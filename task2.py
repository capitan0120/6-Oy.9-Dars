class Solution:
    def judgeCircle(self, moves: str) -> bool:
        L,R,U,D=0,0,0,0
        for move in moves:
            if move=='L':
                L+=1
            if move=='R':
                R+=1
            if move=='D':
                D+=1
            if move=='U':
                U+=1
        return L==R and U==D