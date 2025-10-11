class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=nums.copy()
        while val in a:
            a.remove(val)
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)
        