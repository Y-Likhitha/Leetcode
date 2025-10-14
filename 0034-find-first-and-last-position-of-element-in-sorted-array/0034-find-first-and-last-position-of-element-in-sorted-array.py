class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index=[]
        a=[]
        for i in range(len(nums)):
            if nums[i]==target:
                index.append(i)
        if len(index)==0:
            return [-1,-1]
        else:
            a.append(index[0])
            a.append(index[-1])
            return a
        