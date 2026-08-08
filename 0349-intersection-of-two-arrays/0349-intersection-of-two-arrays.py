class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        i=j=0
        ans=set()
        result=[]
        while i<n1 and j <n2:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums2[j]<nums1[i]:
                j+=1
            else:
                ans.add(nums1[i])
                i+=1
                j+=1
                
               
        for x in ans:
            result.append(x)
        return result
        