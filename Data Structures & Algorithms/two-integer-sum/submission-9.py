class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {num:i for i, num in enumerate(nums)}

        for j in range(len(nums)):
            remaining = target - nums[j]
            if remaining in num_dict and j != num_dict[remaining]:
                return [j, num_dict[remaining]]
