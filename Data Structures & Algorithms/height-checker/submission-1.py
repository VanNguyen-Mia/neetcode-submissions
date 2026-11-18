class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101
        for h in heights:
            counts[h] += 1
        
        expected = []
        for h in range(1, 101):
            c = counts[h]
            for _ in range(c):
                expected.append(h)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
