class Solution {
  public:
    int firstPosition(vector<int>& arr, int target) {
        int start = 0, end = arr.size() - 1, ans = -1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == target) {
                ans = mid;
                end = mid - 1;
            }
            else if (arr[mid] > target) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        return ans;
    }
    int lastPosition(vector<int>& arr, int target) {
        int start = 0, end = arr.size() - 1, ans = -1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == target) {
                ans = mid;
                start = mid + 1;
            }
            else if (arr[mid] > target) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        return ans;
    }
    int countFreq(vector<int>& arr, int target) {
        int firstOccurence = firstPosition(arr, target);
        if (firstOccurence == -1)   return 0;
        int lastOccurence = lastPosition(arr, target);
        return lastOccurence - firstOccurence + 1;
    }
};
