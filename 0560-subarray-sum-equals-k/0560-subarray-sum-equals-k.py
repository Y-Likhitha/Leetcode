class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=0
        c=0
        freq={}
        freq[0]=1
        for i in nums:
            ps+=i
            if ps in freq:
                freq[ps]+=1
            else:
                freq[ps]=1
            if ps-k in freq:
                c+=freq[ps]
        return(c)
        