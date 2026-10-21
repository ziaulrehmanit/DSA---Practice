class Solution {
  public:
    string compareFive(int n) {
        if (n==5){
            return "Equal to 5";
        }
        else if (n<=5){
            return "Less than 5";
        }
        else {
            return "Greater than 5";
        }
    }
};
