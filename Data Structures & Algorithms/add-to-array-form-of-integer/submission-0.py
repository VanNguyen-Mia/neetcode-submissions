class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        total = 0
        exp = len(num) - 1
        for i, n in enumerate(num):
            total += n*(10**(exp-i))
        
        total += k
        res = []
        reversed_res = []
        while total != 0:
            res.append(total % 10)
            total //= 10
        
        while res:
            reversed_res.append(res.pop())
        
        return reversed_res

            
            
