class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and j < len(nums2)-1:
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            res.append(nums2[k])
                            break
                    else:
                        res.append(-1)
                    break
                elif nums1[i] == nums2[j] and j == len(nums2)-1:
                    res.append(-1)
                    break
            
        return res
                            