class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        b = prices[0]
        for sell in prices:
            p = max(p,sell-b)
            b = min(b,sell)
        return p
