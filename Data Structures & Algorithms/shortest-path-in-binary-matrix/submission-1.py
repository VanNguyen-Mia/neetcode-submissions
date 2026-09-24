class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        RC = len(grid)
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        if grid[0][0] != 0 or grid[RC-1][RC-1] != 0:
            return -1
        
        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == RC - 1 and c == RC - 1:
                    return length
            
                directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (min(new_r, new_c) < 0 or
                        new_r == RC or new_c == RC or
                        (new_r, new_c) in visit or
                        grid[new_r][new_c] == 1):
                        continue

                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))
            length += 1
        
        return -1
        