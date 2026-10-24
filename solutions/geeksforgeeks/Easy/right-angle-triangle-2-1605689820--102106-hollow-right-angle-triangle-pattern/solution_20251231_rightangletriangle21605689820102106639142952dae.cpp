void triangle(int s) {

    for (int i=1; i<=s; i++){
        for (int j=1; j<=i; j++){
            if (j==1 || i==s || j==i){
                cout<<"* "<<"";
            }
            else{
                cout<<"  "<<"";
            }
        }
        cout<<endl;
    }
    
}
