class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        res = 0

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else: 
                count -= 1

        return res

# Approach 2:
        # nums.sort()

        # major_num = nums[0]
        # max_count = 0

        # cur_num = nums[0]
        # cur_count = 0

        # for i in range(len(nums)):
        #     if nums[i] == cur_num:
        #         cur_count += 1
        #     else: 
        #         cur_count = 1
        #         cur_num = nums[i]
            
        #     if cur_count > max_count:
        #         max_count = cur_count
        #         major_num = nums[i]
        
        # return major_num
                


# Approach 1:
        # num_counts = {}

        # for num in nums:
        #     if num not in num_counts:
        #         num_counts[num] = 1
        #     else:
        #         num_counts[num] += 1

        # for num, count in num_counts.items():
        #     if count > (len(nums)/2):
        #         return num