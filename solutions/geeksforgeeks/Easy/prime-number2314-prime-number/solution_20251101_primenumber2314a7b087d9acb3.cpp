#include<string>
#include<cmath>
class Solution {
  public:
    string isPrime(int n) {
        string res="Yes";
        if(n<=1){
            res = "No";
        }
        else{
            for (int i = 2; i <= sqrt(n); i++) {
            if (n%i==0){
                res="No";
                break;}      
            }
        }
        return res;  
    }
};
