class Solution:
    def numberOfGasStationsRequired(self, arr, mid):
        cnt = 0
        for i in range(len(arr)-1):
            numberInBetween = int((arr[i+1] - arr[i]) / mid)
            if numberInBetween == (arr[i+1] - arr[i]) / mid:
                numberInBetween -= 1
            cnt += numberInBetween
        return cnt
        
    def minMaxDist(self, stations, k):
        low = high = 0.0
        for i in range(len(stations)-1):
            high = max(high, float(stations[i+1] - stations[i]))
        while high - low > 1e-6:
            mid = (low + high) / 2.0
            cnt = self.numberOfGasStationsRequired(stations, mid)
            if cnt > k:
                low = mid
            else:
                high = mid
        return high
