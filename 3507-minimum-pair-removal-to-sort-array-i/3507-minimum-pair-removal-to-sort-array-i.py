class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c=0
        while True:
                rc=0
                nc=nums.copy()
                nc.sort()
                if (nc==nums)==True:
                    return c
                minsum=[]
                for i in range(len(nums)):
                    if i==len(nums)-1:
                        break
                    minsum.append(nums[i]+nums[i+1])
                minindex=minsum.index(min(minsum))
                while rc!=2:
                    nums.pop(minindex)
                    rc+=1
                nums.insert(minindex,min(minsum))
                c+=1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna