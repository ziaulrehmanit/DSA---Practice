int LCM(int a, int b) {
    
    int product=a*b;
    while (b!=0){
        int temp=b;
        b=a%b;
        a=temp;
    }
    int lcm=product/a;
    return lcm;
}
