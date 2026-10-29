class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        value_dict = {}
        for i in range(len(nums2)):
            value_dict[nums2[i]] = i
        
        mapping = []
        for i in range(len(nums1)):
            mapping.append(value_dict[nums1[i]])
        
        return mapping


