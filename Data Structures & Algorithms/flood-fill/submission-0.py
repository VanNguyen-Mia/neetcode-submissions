class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]

        def dfs(image, sr, sc, visit, origin, color):
            ROWS, COLS = len(image), len(image[0])

            # Base cases:
            if (min(sr, sc) < 0 or
                sr == ROWS or sc == COLS or
                (sr, sc) in visit or
                image[sr][sc] != origin):
                return

            if image[sr][sc] == origin:
                image[sr][sc] = color
            
            visit.append((sr, sc))

            dfs(image, sr + 1, sc, visit, origin, color)
            dfs(image, sr - 1, sc, visit, origin, color)
            dfs(image, sr, sc + 1, visit, origin, color)
            dfs(image, sr, sc - 1, visit, origin, color)

            visit.remove((sr, sc))

        visit = []
        dfs(image, sr, sc, visit, origin, color)
        return image
        