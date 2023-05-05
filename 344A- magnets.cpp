#include <iostream>
using namespace std;
 
 
int main() {
int res = 1;
int t;
cin >>t;
int init;
cin >> init;
 
for(int i=0; i<t-1;i++){
    int n;
    cin >> n;
    if(n!=init){
        res++;
    }
    init = n;
}
cout << res;
return 0;
}
