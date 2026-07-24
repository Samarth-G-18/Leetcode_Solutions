
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # Helper function to find the number of subarrays with AT MOST 'goal' distinct elements
        def at_most(nums: List[int], goal: int) -> int:
            if goal < 0:
                return 0
                
            count = defaultdict(int)
            left = 0
            distinct = 0
            result = 0
            
            for right in range(len(nums)):
                # Expand the window from the right
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1
                
                # Shrink the window from the left if distinct elements exceed goal
                while distinct > goal:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                        distinct -= 1
                    left += 1
                
                # Add the number of valid subarrays ending at 'right'
                result += (right - left + 1)
                
            return result

        # Exactly K = (At Most K) - (At Most K - 1)
        return at_most(nums, k) - at_most(nums, k - 1)
