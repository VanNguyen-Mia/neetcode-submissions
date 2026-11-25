class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counts = [0]*1001
        for i in range(len(counts)):
            for num in nums:
                if num >= i:
                    counts[i] += 1
            if counts[i] == i:
                return i
            if counts[i] == 0:
                break
        return -1