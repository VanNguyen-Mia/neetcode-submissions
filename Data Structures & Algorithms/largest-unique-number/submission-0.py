class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_counts = {}
        largest = -1

        for num in nums:
            if num not in num_counts.keys():
                num_counts[num] = 1
            else:
                num_counts[num] += 1

        for key, val in num_counts.items():
            if val == 1 and key > largest:
                largest = key
        
        return largest
        
        


        