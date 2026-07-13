class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
  
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        p = n - 1  # Start filling from the back
    
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
        
            if left_square > right_square:
                result[p] = left_square
                left += 1
            else:
                result[p] = right_square
                right -= 1
            p -= 1
        
        return result

        