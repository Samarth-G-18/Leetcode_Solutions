class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # If the length shrinks, it means a duplicate was removed!
        return len(nums) != len(set(nums))



        