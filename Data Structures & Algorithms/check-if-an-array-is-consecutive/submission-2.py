class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        is_consecutive = True
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i+1]:
                is_consecutive = False
        return is_consecutive