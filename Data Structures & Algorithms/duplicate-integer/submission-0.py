class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            a = nums[i]
            b = nums.count(a)
            if b > 1:
                return True



        return False