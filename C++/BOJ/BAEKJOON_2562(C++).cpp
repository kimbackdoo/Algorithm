#include <iostream>
using namespace std;

int main(){
	int max=0, c, a[9];
	for(int i=0; i<9; i++){
		cin >> a[i];
		if(max<a[i]){
			max=a[i];
			c = i+1;
		}
	}
	cout << max << endl << c << endl;
	return 0;
}