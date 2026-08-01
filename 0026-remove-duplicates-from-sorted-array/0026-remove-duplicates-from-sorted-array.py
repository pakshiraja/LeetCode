class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        s=set(nums)
        index=0
        for x in sorted(s):
            nums[index]=x
            index+=1
        return index
        