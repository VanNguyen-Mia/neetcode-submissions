class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_1, max_2 = arr[-1], arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > max_1:
                max_1 = arr[i]
            arr[i] = max_2
            max_2 = max_1
        arr[-1] = -1
        return arr

