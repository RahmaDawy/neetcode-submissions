class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       maxPr=0
       minbuy=prices[0]

       for sell in prices :
          maxPr=max(maxPr,sell-minbuy)
          minbuy=min(minbuy,sell)
       return maxPr
