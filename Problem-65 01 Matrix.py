# 542. 01 Matrix

# Time Complexiety: O(n*m)
# Space Complexiety: O(n*m)

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        level = 0

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] = -1
                elif mat[i][j] == 0:
                    q.appendleft((i, j))

        while q:
            size = len(q)

            for _ in range(size):
                cur = q.pop()
                for dir in dirs:
                    nr = cur[0] + dir[0]
                    nc = cur[1] + dir[1]
                    if (
                        nr >= 0
                        and nc >= 0
                        and nr < n
                        and nc < m
                        and mat[nr][nc] == -1
                    ):
                        mat[nr][nc] = level + 1
                        q.appendleft((nr, nc))
            level += 1

        return mat
