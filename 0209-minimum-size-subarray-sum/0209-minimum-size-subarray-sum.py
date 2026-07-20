class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsub = float('inf')
        cur,i=0,0
        for j in range(len(nums)):
            cur+=nums[j]

            while cur>=target:
                current_length = j - i+ 1
                minsub = min(minsub, current_length)
                cur-=nums[i]
                i+=1

        return minsub if minsub != float('inf') else 0

                



        