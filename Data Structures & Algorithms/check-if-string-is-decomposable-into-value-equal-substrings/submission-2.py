class Solution:
    def isDecomposable(self, s: str) -> bool:
        s = s + "."
        num = s[0]
        length, count_two = 0, 0

        for i in range(len(s)):
            if s[i] == num:
                length += 1
            else:
                num = s[i]
                if length % 3 == 1:
                    return False
                elif length % 3 == 2:
                    count_two += 1
                    if count_two > 1:
                        return False
                length = 1
        
        # if length % 3 == 1:
        #     return False
        # elif length % 3 == 2:
        #     count_two += 1
        #     if count_two > 1:
        #         return False
        if count_two < 1:
            return False
        return True

        
            
