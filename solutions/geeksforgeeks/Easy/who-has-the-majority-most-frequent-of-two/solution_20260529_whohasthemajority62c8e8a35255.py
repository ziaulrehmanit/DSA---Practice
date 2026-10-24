class Solution:
    def moreFrequent(self, arr, x, y):
        
        freq_of_x = 0
        freq_of_y = 0
        
        for num in arr:
            
            if num == x:
                freq_of_x += 1
            if num == y:
                freq_of_y += 1
        
        if freq_of_x > freq_of_y:
            return x
        elif freq_of_y > freq_of_x:
            return y
        else:
            return min(x, y)
