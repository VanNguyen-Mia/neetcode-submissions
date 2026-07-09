class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
                    ")": "(",
                    "]": "[",
                    "}": "{"
                }
        stack = []
        for b in s:
            if b in pairs.values():
                stack.append(b)
            elif not stack or stack[-1] != pairs[b]:
                return False
            else:
                stack.pop()
        return not stack
