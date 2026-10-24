class Solution {
  public:
    bool isSorted(vector<int>& arr) {
        
        bool result = true;
        for (int i=1; i<arr.size(); i++)
        {
            if (arr[i]<arr[i-1])
            {
                result = false;
                break;
            }
        }
        return result;
    }
};
