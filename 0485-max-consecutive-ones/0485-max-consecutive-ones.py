class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxo=0
        count=0
        for num in nums:
            if num==0:
                count=0
            else:
                count+=1
            maxo=max(count,maxo)


        return maxo

        