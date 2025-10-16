class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l=[]
        maxsum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                    a=nums[i:j].copy()
                    a.sort()
                    if nums[i:j]==a and sum(nums[i:j])>maxsum:
                        if len(list(set(nums[i:j])))==len(a):
                                print(nums[i:j])
                                maxsum=sum(nums[i:j])
        return maxsum
        