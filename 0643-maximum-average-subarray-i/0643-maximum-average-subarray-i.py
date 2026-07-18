class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       # 1. Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
    
    # 2. Slide the window across the rest of the array
        for i in range(k, len(nums)):
        # Add the next element, subtract the element leaving the window
            current_sum += nums[i] - nums[i - k]
        # Keep track of the highest sum seen
            max_sum = max(max_sum, current_sum)
        
    # 3. Return the maximum average
        return max_sum / k

    
    
    

        