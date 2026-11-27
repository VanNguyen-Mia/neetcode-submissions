class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts.keys():
                counts[num] = 1
            else:
                counts[num] += 1
        lst = [[num, count] for num, count in counts.items()]        
        lst.sort(key= lambda x: (x[1], -x[0]))
        res = []
        for t in lst:
            while t[1] > 0:
                res.append(t[0])
                t[1] -= 1
        return res

        