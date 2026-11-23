class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        repeated = set()
        for num in nums2:
            if num in nums1:
                repeated.add(num)
        res = [num for num in repeated]
        return res
        