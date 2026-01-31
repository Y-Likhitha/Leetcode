class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nl=list(str(n))
        nl=[a for a in nl if a!='0']
        x=(''.join(nl))
        sums=0
        for i in x:
            sums+=int(i)
        return(int(x)*sums)
        