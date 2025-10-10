class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cl=nums1+nums2
        cl.sort()
        if len(cl)%2!=0:
            return cl[len(cl)//2]
        else:
            a=len(cl)//2
            i=(cl[a]+cl[a-1])/2
            return i


        