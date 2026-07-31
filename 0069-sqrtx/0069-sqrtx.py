class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2: return x
        st,end=0,x
        
        while st<=end:
            mid=st+(end-st)//2
            sq=mid*mid
            if sq==x:
                return mid
            if sq<x:
                st=mid+1
            else:
                end=mid-1
        return end

       
        
        