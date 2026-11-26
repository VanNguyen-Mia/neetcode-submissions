class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res1 = []
        for num2 in arr2:
            for num1 in arr1:
                if num1 == num2:
                    res1.append(num1)
        res2 = []
        for num1 in arr1:
            if num1 not in res1:
                res2.append(num1)
        res2.sort()
        return res1 + res2