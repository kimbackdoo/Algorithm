#include <iostream>
using namespace std;

int main(){
	int t, a, b, arr[100];
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> a >> b;
		arr[i]=a+b;
	}
	for(int i=0; i<t; i++)
		cout << arr[i] << endl;
	return 0;
}