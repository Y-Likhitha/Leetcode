class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rnums=nums.copy()
        rnums.reverse()
        import math
        leftSum=[]
        rightSum=[]
        ans=[]
        for i in range(len(nums)):
            sl=0
            sr=0
            if i==0:
                leftSum.append(0)
                rightSum.append(0)
                continue
            sl+=leftSum[-1]+nums[i-1]
            sr+=rightSum[-1]+rnums[i-1]
            leftSum.append(sl)
            rightSum.append(sr)
        rightSum.reverse()
        for i in range(0,len(nums)):
            ans.append(math.fabs(leftSum[i]-rightSum[i]))
        return(list(map(int,ans)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna