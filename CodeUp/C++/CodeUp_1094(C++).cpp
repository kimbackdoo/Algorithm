#include <iostream>
using namespace std;

int main(){
	int n, t;
	int a[10001]={};
	cin >> n;
	for(int i=1; i<=n; i++){
		cin >> t;
		a[i] = t;
	}
	for(int i=n; i>=1; i--)
		cout << a[i] << " ";
	cout << endl;
	return 0;
}