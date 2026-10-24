class Solution {
  public:
    void printTable(int n) {
        int multiplier = 10;
        while (multiplier>0) {
            cout<<n*multiplier<<" ";
            multiplier-=1;
        }

        cout << endl;
    }
};
