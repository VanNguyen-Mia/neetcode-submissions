class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_list = []

        for i in range(len(s)):
            s_list.append([s[i], i])
        
        for change in shift:
            if change[0] == 1:
                for letter in s_list:
                    letter[1] += change[1]
                    letter[1] = letter[1] % len(s)
            else:
                for letter in s_list:
                    letter[1] -= change[1]
                    letter[1] = letter[1] % len(s)

        new_s = "".join(letter for letter, position in sorted(s_list, key=lambda x: x[1]))
        return new_s
        
        