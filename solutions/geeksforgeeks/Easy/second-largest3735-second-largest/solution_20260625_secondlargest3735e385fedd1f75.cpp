class Solution {
  public:
    int getSecondLargest(vector<int> &arr) {
        
        int largest,secondLargest;
        largest=secondLargest=-1;
        
        int size=arr.size();
        
        for (int i=0; i<size; i++)
        {
            if (arr[i]>largest)
            {
                secondLargest=largest;
                largest=arr[i];
            }
            else if (arr[i]>secondLargest && arr[i]!=largest)
            {
                secondLargest=arr[i];
            }
        }
        return secondLargest;
    }
};
