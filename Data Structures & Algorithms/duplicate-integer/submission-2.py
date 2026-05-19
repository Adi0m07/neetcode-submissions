class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2=tuple(nums)
        a=set(num2)
        print(a)
        if len(a) == len(nums):
            return False



        return True