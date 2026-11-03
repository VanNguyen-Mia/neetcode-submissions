class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        strs.sort(key=lambda x: len(x))
        if strs[0] == "":
            return common_prefix

        shortest = strs[0]
        for i in range(len(shortest)):
            is_common = True
            for j in range(1, len(strs), 1):
                if strs[j][i] == shortest[i]:
                    is_common = True
                else:
                    is_common = False
                    break
            if is_common:
                common_prefix += shortest[i]
            else:
                break

        return common_prefix
