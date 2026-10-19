class Solution {
  public:
    string isVowel(char c) {
        if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u'){
            return "YES";
        }
        else if (c=='A' || c=='E' || c=='I' || c=='O' || c=='U'){
            return "YES";
        }
        else{
            return "NO";
        }
    }
};
