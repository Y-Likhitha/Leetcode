class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums1=nums.copy()
        nums1.sort()
        l=0
        r=len(nums)-1
        a=[]
        while l<len(nums1):
            if nums1[l]+nums1[r]==target:
                a.append(nums1[l])
                a.append(nums1[r])
                break
            elif nums1[l]+nums1[r]<target:
                l+=1
            else:
                r-=1
        for i in range(len(nums)):
            if nums[i] in a:
                ans.append(i)
        return(ans)

        