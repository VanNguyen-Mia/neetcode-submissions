class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1, min1 = max(nums), min(nums)
        nums.remove(max1)
        nums.remove(min1)
        max2 = max(nums)
        min2 = min(nums)
        res = (max1*max2) - min1*min2
        return res