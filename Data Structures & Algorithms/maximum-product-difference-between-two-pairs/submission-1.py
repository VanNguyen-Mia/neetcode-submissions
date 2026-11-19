class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = 100000

        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return (max1*max2) - (min1*min2)


# approach 1:
        # max1, min1 = max(nums), min(nums)
        # nums.remove(max1)
        # nums.remove(min1)
        # max2 = max(nums)
        # min2 = min(nums)
        # res = (max1*max2) - min1*min2
        # return res