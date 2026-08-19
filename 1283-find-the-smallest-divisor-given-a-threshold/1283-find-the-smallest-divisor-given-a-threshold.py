class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def guess(divisor,nums):
            res=0
            for i in range(len(nums)):
                res+=math.ceil(nums[i]/divisor)
            return res

        low,high=1,max(nums)
        while low<high:
            mid=low+(high-low)//2
            if guess(mid,nums)<=threshold:
                high=mid
            else:
                low=mid+1
        return low
        