class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum = 0
        max_consecutive = 0
        for num in nums:
            if num == 1:
                sum += 1
                if sum > max_consecutive:
                    max_consecutive = sum
            else:
                sum = 0
        return max_consecutive


                

        