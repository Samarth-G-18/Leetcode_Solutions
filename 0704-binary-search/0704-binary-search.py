class Solution:

  def search(self, nums: list[int], target: int) -> int:
    st, end = 0, len(nums) - 1

    while st <= end:
      mid = (st + end) // 2

      if nums[mid] == target:
        return mid  # Returns the index of the target
      elif nums[mid] > target:
        end = mid - 1
      else:
        st = mid + 1

    return -1  # Target not found



        