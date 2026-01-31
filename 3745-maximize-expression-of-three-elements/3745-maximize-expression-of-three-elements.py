class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return (nums[0])
        maxnum=max(nums)
        numslist=list(map(str,nums))
        numslist.remove(str(maxnum))
        numslist=list(map(int,numslist))
        maxnum1=max(numslist)
        minnum=min(numslist)
        return(maxnum+maxnum1-minnum)
    
                