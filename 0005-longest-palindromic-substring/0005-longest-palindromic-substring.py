class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        maxlen=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if len(s[i:j])>maxlen:
                        maxlen=len(s[i:j])
                        l.append(s[i:j])
        return (l[-1])
    

        
        