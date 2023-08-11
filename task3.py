class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        filter = []
        for r in range(m):
            row = []
            for c in range(n):
                avg = 0
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if r + i >= 0 and r + i < m and j + c >= 0 and j + c < n:
                            count += 1
                            avg += img[r + i][c + j]
                row.append(avg // count)
            filter.append(row)

        return filter