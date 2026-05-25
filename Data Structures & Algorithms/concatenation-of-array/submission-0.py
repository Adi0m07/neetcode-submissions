class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l1 =[]
        for i in range(len(nums)):
            l1.append(nums[i])
        for j in range(len(nums)):
            l1.append(nums[j])
        return l1