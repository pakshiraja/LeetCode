class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        f=0
        for ele in arr:
            if ele in freq:
                freq[ele]+=1
            else:
                freq[ele]=1
        l=list(freq.values())
        s=set(freq.values())
        if len(s)==len(l):
            return True
        return False