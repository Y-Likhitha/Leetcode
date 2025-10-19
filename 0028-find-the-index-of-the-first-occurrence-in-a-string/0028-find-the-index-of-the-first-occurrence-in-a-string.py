class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length=len(needle)
        l=[]
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            for j in range(i+1,len(haystack)):
                if haystack[i:j+1]==needle:
                    return i