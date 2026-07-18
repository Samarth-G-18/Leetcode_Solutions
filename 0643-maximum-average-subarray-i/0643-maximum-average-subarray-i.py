class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur=sum(nums[0:k])
        maxi=cur
        for i in range(k,len(nums)):
            cur+=nums[i]-nums[i-k]
            maxi=max(maxi,cur)
        return maxi/k


        