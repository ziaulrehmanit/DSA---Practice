#include<string>
class Solution {
  public:
    void arrayTraversalReverse(int numbers[], int size) {
        string str="";
        int a;
        for(int j=size-1;j>=0;j--){
            a=numbers[j];
            str += to_string(a);
            str += " ";
        }
        cout<<str;
    }
};
