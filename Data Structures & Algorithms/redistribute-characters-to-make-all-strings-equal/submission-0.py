class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}
        for word in words:
            for letter in word:
                if letter not in count.keys():
                    count[letter] = 1
                else:
                    count[letter] += 1
                    
        n = len(words)
        for value in count.values():
            if value % n != 0:
                return False
        return True