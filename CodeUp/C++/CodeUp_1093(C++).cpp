#include <iostream>
using namespace std;

int main(){
	int n, t;
	int a[24]={};
	cin >> n;
	for(int i=1; i<=n; i++){
		cin >> t;
		a[t]+=1;
	}
	for(int i=1; i<24; i++)
		cout << a[i] << " ";
	cout << endl;
	return 0;
}