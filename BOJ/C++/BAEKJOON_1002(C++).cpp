#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int t, x1,y1,r1,x2,y2,r2;
	cin >> t;
	for(int i=0; i<t; i++){
		cin>>x1>>y1>>r1>>x2>>y2>>r2;
		double d=sqrt(pow(x2-x1,2)+pow(y2-y1,2));
		if(x1==x2&&y1==y2){
			if(r1==r2) cout << -1 << endl;
			else cout << 0 << endl; 
		}
		else if(abs(r2-r1)<d&&d<r2+r1) cout << 2 << endl;
		else if(d==r2+r1||d==abs(r2-r1)) cout << 1 << endl;
		else cout << 0 << endl;
	}
	return 0;
}