class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]==0:
                ele=nums[l]
                nums.remove(nums[l])
                nums.append(ele)
                r-=1
            else:
                l+=1

        