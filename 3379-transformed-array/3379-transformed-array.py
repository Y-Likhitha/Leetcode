class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(nums[(i+nums[i])%len(nums)])
        return(res)
        
    
        
        
        
        