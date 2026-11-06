class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        len_increase = len_decrease = len_longest = 1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                len_increase += 1
                len_decrease = 1
                if len_increase > len_longest:
                    len_longest = len_increase
            elif nums[i] < nums[i+1]:
                len_decrease += 1
                len_increase = 1
                if len_decrease > len_longest:
                    len_longest = len_decrease
            else:
                len_increase = 1
                len_decrease = 1

        return len_longest
        

            