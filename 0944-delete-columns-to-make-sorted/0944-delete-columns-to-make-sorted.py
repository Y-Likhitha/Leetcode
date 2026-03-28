class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
            cols=[]
            lexorder=[]
            count=0
            for i in range(0,len(strs[0])):
                l=[]
                a=[]
                for j in strs:
                        a.append(ord(j[i]))
                        l.append(j[i])
                cols.append(l)
                lexorder.append(a)
            # print(cols)
            # print(lexorder)
            for i in range(len(lexorder)):
                a=lexorder[i].copy()
                a.sort()
                if a!=lexorder[i]:
                    count+=1
            return(count)
                
        