class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k_list = []
        while low <= high:
            k = (low + high)// 2
            total_time = self.totalTime(k, piles)
            if total_time > h:
                low = k + 1
            elif total_time <= h:
                high = k - 1
                k_list.append(k)
        return min(k_list)
                
    def totalTime(self, k, piles):
        total_time = 0
        for pile in piles:
            time = pile // k 
            remaining = pile % k
            if remaining != 0:
                time += 1
            total_time += time
        return total_time