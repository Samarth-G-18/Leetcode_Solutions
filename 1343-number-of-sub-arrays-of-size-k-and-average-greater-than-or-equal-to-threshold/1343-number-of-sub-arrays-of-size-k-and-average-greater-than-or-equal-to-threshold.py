class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur=sum(arr[:k])
        no_sub= 1 if (cur / k) >= threshold else 0
        for i in range(k,len(arr)):
            cur+=arr[i]-arr[i-k]
            if cur/k>=threshold:
                no_sub+=1

        return no_sub


        