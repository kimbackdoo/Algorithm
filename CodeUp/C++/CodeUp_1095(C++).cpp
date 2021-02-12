#include <iostream>
using namespace std;

int main(){
	int n, k, t;
	int a[10001]={};
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> k;
		a[i] = k;
	}
	t = a[0];
	for(int i=0; i<n; i++)
		if(t>a[i])
			t=a[i];
	cout << t << endl;
	return 0;
}