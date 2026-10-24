class Solution {
  public:
  
    bool isVowel(char c){
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        {
            return true;
        }
        return false;
    }
    
    string modify(string& s) {
        
        int left = 0;
        int right = s.size() - 1;
        
        while (left < right)
        {
            if (isVowel(s[left]) && isVowel(s[right]))
            {
                char temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left += 1;
                right -= 1;
            }
            else if (isVowel(s[left]))
            {
                right -= 1;
            }
            else if (isVowel(s[right]))
            {
                left += 1;
            }
            else
            {
                left += 1;
                right -= 1;
            }
        }
        return s;
    }
};
