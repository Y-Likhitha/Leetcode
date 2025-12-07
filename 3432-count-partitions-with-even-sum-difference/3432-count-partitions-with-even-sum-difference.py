class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                second=(nums[j:len(nums)])
                first=nums[i:j]
                sumf=sum(first)
                sums=sum(second)
                if sumf>sums and (sumf-sums)%2==0:
                    print(sumf,sums,sumf-sums)
                    c+=1
                elif sumf<sums and (sums-sumf)%2==0:
                    print(sumf,sums,sums-sumf)
                    c+=1
                elif sumf-sums==0:
                    c+=1
            break
        return c
        