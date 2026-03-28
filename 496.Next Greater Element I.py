class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = {}

        for i in range(len(nums2)-1,-1,-1) :

            while stack and stack[-1] <= nums2[i] :
                stack.pop()

            if not stack :
                hmap[nums2[i]] = -1
                
            
            else :
                hmap[nums2[i]] = stack[-1]
                
            stack.append(nums2[i])
                
        return [hmap[x] for x in nums1]
        
