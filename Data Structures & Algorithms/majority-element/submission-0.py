class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1
        for num, count in num_counts.items():
            if count > (len(nums)/2):
                return num