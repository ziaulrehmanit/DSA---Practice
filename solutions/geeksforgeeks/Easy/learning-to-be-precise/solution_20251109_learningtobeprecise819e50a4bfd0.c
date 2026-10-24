#include<iomanip>
void precise(float a, float b) {
    
    float c = a/b;
    
    cout << c << " " << fixed << setprecision(3) << c << endl;
}
