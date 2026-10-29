class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        
        for num in nums1:
            for i in range(len(nums2)):
                if num == nums2[i]:
                    mapping.append(i)
                    break
        return mapping


