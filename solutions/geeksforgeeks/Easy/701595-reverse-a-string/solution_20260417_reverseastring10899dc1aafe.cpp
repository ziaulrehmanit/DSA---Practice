class Solution {
  public:
    string reverseString(string& s) {
        
        int left = 0;
        int right = s.size() - 1;
        char temp;
        
        while (left < right){
            
            temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            
            left += 1;
            right -= 1;
        }
        
        return s;
    }
};
