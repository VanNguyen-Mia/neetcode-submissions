class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):
            j = i - 1
            while j >= 0 and heights[j] < heights[j+1]:
                tmp1 = heights[j]
                heights[j] = heights[j+1]
                heights[j+1] = tmp1

                tmp2 = names[j]
                names[j] = names[j+1]
                names[j+1] = tmp2
                
                j -= 1
        return names



# Approach 1:
        # map = {}
        # for i in range(len(names)):
        #     map[heights[i]] = names[i]
        # names = []
        # heights.sort(reverse = True)
        # for height in heights:
        #     names.append(map[height])
        # return names