# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        n = len(pairs)
        for i in range(n):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                tmp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = tmp
                j -= 1 
            result.append(copy.deepcopy(pairs)) 

        return result