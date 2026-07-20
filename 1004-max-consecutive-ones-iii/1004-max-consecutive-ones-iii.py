class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxsub=0
        i,cnt=0,0
        for j in range(i,len(nums)):
            if nums[j]==0:
                cnt+=1

            while cnt>k:
                if nums[i]==0:
                    cnt-=1
                i+=1
            maxsub=max(maxsub,j-i+1)

        return maxsub
                



        