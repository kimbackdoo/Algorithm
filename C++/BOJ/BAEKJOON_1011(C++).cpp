#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int t, x, y;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> x >> y;
		long long k=1;
		for(; k*k<=(y-x); k++){}
		k--;
		long long tmp = (y-x)-(k*k);
		tmp=(long long)ceil((double)tmp/k);
		cout << k*2-1+tmp << endl;
	}
	return 0;
}