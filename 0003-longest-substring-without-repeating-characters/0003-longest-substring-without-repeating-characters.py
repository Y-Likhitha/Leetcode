class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=list(s)
        print(l)
        ans=[]
        a=[]
        ans1=[]
        for i in range(len(l)):
            if l[i] not in ans:
                ans.append(l[i])
                a.append(len(ans))
            else:
                while l[i] in ans:
                    ans.pop(0)
                ans.append(l[i])
                a.append(len(ans))
        if len(a)==0:
            return 0
        else:
            return max(a)        