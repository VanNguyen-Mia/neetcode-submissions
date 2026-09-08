class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            remaining = first - second
            if remaining != 0:
                heapq.heappush(stones, remaining)
        
        return abs(stones[0]) if stones else 0

