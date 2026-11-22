class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        count = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
                res.append(nums[i])
        
        for num in range(1, len(nums) + 1):
            if num not in count:
                res.append(num)
                break

        return res
        