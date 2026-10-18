class Solution {
public:

    bool isVowel(char c)
    {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
    string reverseVowels(string s) {

        int left = 0;
        int right = s.size() - 1;
        char temp;

        while (left < right)
        {
            if (isVowel(s[left]) && isVowel(s[right]))
            {
                temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left += 1;
                right -= 1;
            }
            else if (!isVowel(s[left]))
                left += 1;

            else
                right -= 1;                
        }
        return s;

    }
};
