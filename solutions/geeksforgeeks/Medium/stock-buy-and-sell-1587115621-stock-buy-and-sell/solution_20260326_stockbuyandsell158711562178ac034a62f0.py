class Solution:
    
    def stockBuySell(self, arr):
        
        minimum_price = arr[0]
        maximum_profit = 0

        for i in range(1,len(arr)):

            if minimum_price > arr[i]:
                minimum_price = arr[i]

            else:
                maximum_profit += arr[i] - minimum_price
                minimum_price = arr[i]

        return maximum_profit
