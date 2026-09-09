class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def get_dict(word):
            word_dict = {}
            for letter in word:
                if letter not in word_dict:
                    word_dict[letter] = 1
                else:
                    word_dict[letter] += 1
            return word_dict
        
        s_dict = get_dict(s)
        t_dict = get_dict(t)

        return s_dict == t_dict
        
        

        
        
        