class Solution {
  public:
    void pushZerosToEnd(vector<int>& arr) {
        
        int number = 0;
        int temp;
        
        for (int i = 0; i < arr.size(); i++)
        {
            if (arr[i]!=0)
            {
                temp = arr[number];
                arr[number] = arr[i];
                arr[i] = temp;
                number++;
            }
        }
    }
};
