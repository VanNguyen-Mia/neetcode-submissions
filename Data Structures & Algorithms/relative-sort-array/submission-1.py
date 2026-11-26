class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = j = 0
        for num in arr2:
            i = j
            while i < len(arr1):
                if arr1[i] == num:
                    tmp = arr1[i]
                    arr1[i] = arr1[j]
                    arr1[j] = tmp
                    j += 1
                i += 1
        arr3 = arr1[j:]
        arr3.sort()
        return arr1[:j] + arr3


# Approach 1:
        # res1 = []
        # for num2 in arr2:
        #     for num1 in arr1:
        #         if num1 == num2:
        #             res1.append(num1)
        # res2 = []
        # for num1 in arr1:
        #     if num1 not in res1:
        #         res2.append(num1)
        # res2.sort()
        # return res1 + res2