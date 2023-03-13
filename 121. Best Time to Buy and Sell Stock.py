class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #slow n^2
        '''
        i = len(prices)-1
    
        maxPr = 0
        while i >= 0:
            j=i-1
            #print("firt while i =",i)
            #print(prices[i])
            while j >= 0:
                profit = prices[i]-prices[j]
                if profit > maxPr:
                    #print('i=',i )
                    #print( 'j=',j)
                    maxPr = profit
                #print(j)
                j-=1  
            i-=1 
        return maxPr
        '''
        #simple approch 
        minPrice = float('inf')
        maxPr = 0
        for i in range(len(prices)):
            #print(prices[i])
            if minPrice > prices[i]:
                minPrice = prices[i]
            if prices[i] - minPrice > maxPr:
                maxPr = prices[i] - minPrice
        return maxPr


        
        
