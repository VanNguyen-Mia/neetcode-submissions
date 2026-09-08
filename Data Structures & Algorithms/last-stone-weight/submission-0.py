class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones[-1]
            y = stones[-2]

            def pop_both(arr):
                arr.pop()
                arr.pop()
            if x == y:
                pop_both(stones)
            else:
                tmp = abs(x - y)
                pop_both(stones)
                stones.append(tmp)

        return stones[0] if stones else 0
