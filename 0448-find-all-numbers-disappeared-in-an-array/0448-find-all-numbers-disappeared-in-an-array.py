class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in numbers:
                res.append(i)
        return res     