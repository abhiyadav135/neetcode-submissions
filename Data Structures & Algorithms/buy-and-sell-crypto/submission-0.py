class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        n=len(prices)
        left,right=0,1
        for i in range(n-1):
            for j in range(i,n):
                curr=prices[j]-prices[i]
                mp=max(curr,mp)
        return mp               

