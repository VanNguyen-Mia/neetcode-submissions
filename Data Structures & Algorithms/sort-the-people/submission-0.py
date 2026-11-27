class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        for i in range(len(names)):
            map[heights[i]] = names[i]
        names = []
        heights.sort(reverse = True)
        for height in heights:
            names.append(map[height])
        return names