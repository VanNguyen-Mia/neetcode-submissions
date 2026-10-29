class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = 1000
        for num in nums:
            if num < min_num:
                min_num = num
        digits = []
        while min_num != 0:
            digit = min_num % 10
            min_num //= 10
            digits.append(digit)
        
        return 1 if (sum(digits)%2==0) else 0
