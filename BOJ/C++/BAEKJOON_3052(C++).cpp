#include <iostream>
using namespace std;

int main(){
	int n, a[42]={}, count=0;
	for(int i=0; i<10; i++){
		cin >> n;
		a[n%42]=1;
	}
	for(int i=0; i<42; i++)
		count += a[i];
	cout << count << endl;
	return 0;
}