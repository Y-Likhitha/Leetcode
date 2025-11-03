class Solution:
    def maxDifference(self, s: str) -> int:
        alpha=list(set(s))
        even=[]
        odd=[]
        ans=[]
        for i in alpha:
            if s.count(i)%2==0:
                even.append(s.count(i))
            else:
                odd.append(s.count(i))
        for i in even:
            ans.append((max(odd)-i))
        return(max(ans))