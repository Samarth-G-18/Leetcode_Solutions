
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize both tracker variables with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # If current_sum becomes negative, reset it by choosing the current number.
            # Otherwise, add the current number to extend the existing subarray.
            current_sum = max(num, current_sum + num)
            
            # Keep track of the highest global sum seen so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum

        