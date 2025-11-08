# 733. Flood Fill

# Time Complexity: O(nm)
# Space Complexity: O(nm)

from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        oldColor = image[sr][sc]
        
        q = deque()
        q.appendleft(sr)
        q.appendleft(sc)
        image[sr][sc] = color
        while q:
            cr = q.pop()
            cc = q.pop()

            for r,c in dirs:
                row = cr + r
                col = cc + c

                if row >= 0 and col >= 0 and row < len(image) and col < len(image[0]) and image[row][col] == oldColor:
                    image[row][col] = color
                    q.appendleft(row)
                    q.appendleft(col)
        
        return image
